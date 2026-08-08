"""Motor de percurso dos nós N0–N11 do algoritmo híbrido.

Uso:
    motor = Motor()
    sessao = Sessao()
    while True:
        passo = motor.avaliar(sessao)
        if isinstance(passo, Resultado):
            break
        sessao.responder(passo.id, valor)  # Pergunta

O percurso é recomputado do zero a cada chamada (stateless/idempotente):
as respostas acumuladas na sessão determinam até onde o fluxo avança e qual
é a próxima pergunta. Quando não falta nenhuma variável, sai um Resultado.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path

from .asa import classificar_asa
from .exames import avaliar_matriz, reforcar
from .perguntas import VARIAVEIS
from .porte import inferir_porte
from .rcri import calcular_rcri

CAMINHO_PROTOCOLO = Path(__file__).resolve().parent.parent / "protocolos" / "triagem-preop-cardiovascular.json"


@dataclass
class Pergunta:
    id: str
    texto: str
    tipo: str
    opcoes: list = None
    no: str = None


@dataclass
class Resultado:
    saida: str  # 'fora_de_escopo' | 'suspender_indicacao' | 'plano'
    motivo: str = None
    asa: str = None
    asa_criterios: list = field(default_factory=list)
    porte: str = None
    rcri: dict = None
    sinalizadores: list = field(default_factory=list)
    exames: dict = field(default_factory=dict)
    plano: list = field(default_factory=list)
    notas: list = field(default_factory=list)
    trajeto: list = field(default_factory=list)


@dataclass
class Sessao:
    respostas: dict = field(default_factory=dict)

    def responder(self, id_variavel, valor):
        if id_variavel not in VARIAVEIS:
            raise ValueError(f"Variável desconhecida: {id_variavel}")
        self.respostas[id_variavel] = valor


class _PerguntaNecessaria(Exception):
    def __init__(self, pergunta):
        self.pergunta = pergunta


class Motor:
    def __init__(self, caminho_protocolo=CAMINHO_PROTOCOLO, config=None):
        with open(caminho_protocolo, encoding="utf-8") as f:
            self.protocolo = json.load(f)
        self.config = {"vigilancia_mins_ativa": True}
        if config:
            self.config.update(config)

    def avaliar(self, sessao):
        """Devolve a próxima Pergunta ou o Resultado final."""
        try:
            return self._executar(sessao.respostas)
        except _PerguntaNecessaria as exc:
            return exc.pergunta

    # ------------------------------------------------------------------
    def _pede(self, r, id_variavel, no):
        if id_variavel in r:
            return r[id_variavel]
        spec = VARIAVEIS[id_variavel]
        raise _PerguntaNecessaria(
            Pergunta(
                id=id_variavel,
                texto=spec["texto"],
                tipo=spec["tipo"],
                opcoes=spec.get("opcoes"),
                no=no,
            )
        )

    def _executar(self, r):
        trajeto = []
        sinalizadores = []
        notas = []
        plano = []

        # ---------------- N0 — contexto ----------------
        trajeto.append("N0")
        idade = self._pede(r, "idade", "N0")
        if idade < 18:
            return Resultado(
                saida="fora_de_escopo",
                motivo="Paciente menor de 18 anos — protocolo restrito a adultos",
                trajeto=trajeto,
            )
        if not self._pede(r, "cirurgia_eletiva", "N0"):
            return Resultado(
                saida="fora_de_escopo",
                motivo="Cirurgia não eletiva — emergência/urgência segue fluxo próprio",
                trajeto=trajeto,
            )

        # ---------------- N1 — instabilidade ----------------
        trajeto.append("N1")
        for var, rotulo in (
            ("sca_recente", "Síndrome coronariana aguda recente"),
            ("ic_descompensada", "Insuficiência cardíaca descompensada"),
            ("arritmia_grave", "Arritmia grave"),
            ("valvopatia_grave_sintomatica", "Valvopatia grave sintomática"),
        ):
            if self._pede(r, var, "N1"):
                sinalizadores.append({"id": "instabilidade_cardiaca", "detalhe": [rotulo]})
                return Resultado(
                    saida="suspender_indicacao",
                    motivo=f"Condição cardíaca instável: {rotulo}",
                    sinalizadores=sinalizadores,
                    plano=[
                        "Suspender fluxo eletivo",
                        "Encaminhamento médico imediato para tratamento/otimização",
                        "Reavaliar indicação cirúrgica após resolução",
                    ],
                    trajeto=trajeto,
                )

        # ---------------- N2 — porte ----------------
        trajeto.append("N2")
        procedimento = self._pede(r, "procedimento", "N2")
        porte = inferir_porte(procedimento) or self._pede(r, "porte", "N2")

        # ---------------- N2b — ASA-PS provisória ----------------
        trajeto.append("N2b")
        for var in (
            "hist_doenca_coronariana", "hist_avc_ait",
        ):
            self._pede(r, var, "N2b")
        if r["hist_doenca_coronariana"] or r["hist_avc_ait"]:
            self._pede(r, "evento_timing", "N2b")
        for var in (
            "insuficiencia_cardiaca_historia", "fe_reduzida", "marcapasso",
            "dialise", "doenca_renal_cronica", "diabetes",
        ):
            self._pede(r, var, "N2b")
        if r["diabetes"] != "nao":
            self._pede(r, "diabetes_insulina", "N2b")
        for var in (
            "hipertensao", "dpoc", "doenca_pulmonar_leve", "hepatite_ativa",
            "alcool", "tabagismo_atual", "imc", "gestacao",
            "limitacao_funcional_substantiva", "outra_doenca",
        ):
            self._pede(r, var, "N2b")

        asa, asa_criterios = classificar_asa(r)
        if r["gestacao"] == "sim":
            notas.append("Gestação confirmada: envolver via obstétrica/anestesia obstétrica no planejamento")
        if asa == "IV":
            sinalizadores.append({"id": "asa_iv_provisorio", "detalhe": asa_criterios})
            return Resultado(
                saida="suspender_indicacao",
                motivo="ASA IV provisório (ameaça constante à vida): " + "; ".join(asa_criterios),
                asa=asa,
                asa_criterios=asa_criterios,
                porte=porte,
                sinalizadores=sinalizadores,
                plano=[
                    "Suspender fluxo eletivo (equivale ao nó N1)",
                    "Encaminhar para otimização clínica da condição de base",
                    "Reavaliar indicação após estabilização",
                ],
                notas=notas,
                trajeto=trajeto,
            )

        # ---------------- N3 — gate do paciente ----------------
        trajeto.append("N3")
        fatores_risco = bool(
            r["tabagismo_atual"]
            or r["diabetes"] != "nao"
            or r["hipertensao"] != "nao"
        )
        doenca_cv = bool(
            r["hist_doenca_coronariana"]
            or r["hist_avc_ait"]
            or r["insuficiencia_cardiaca_historia"]
            or r["fe_reduzida"] in ("moderada", "grave")
            or r["marcapasso"]
        )
        liberado = (
            idade < 65
            and not fatores_risco
            and not doenca_cv
            and porte in ("baixo", "intermediario")
        )

        # ---------------- N4 — fragilidade ----------------
        frail = None
        if idade >= 65:
            trajeto.append("N4")
            frail = self._pede(r, "frail_score", "N4")
            if frail >= 3:
                sinalizadores.append({"id": "fragilidade", "detalhe": f"FRAIL {int(frail)}/5"})

        # ---------------- N5 — capacidade funcional ----------------
        trajeto.append("N5")
        mets = self._pede(r, "mets_4", "N5")
        if mets != "sim":
            sinalizadores.append({
                "id": "pre_habilitacao",
                "detalhe": "Capacidade funcional < 4 METs ou indeterminada — janela da contemplação permite pré-habilitação",
            })
            plano.append("Pré-habilitação antes do agendamento (capacidade funcional baixa/indeterminada)")

        # ---------------- Caminho liberado (gate N3 verdadeiro) ----------------
        if liberado:
            trajeto.append("N11")
            exames = avaliar_matriz(self.protocolo, r, asa, porte, idade)
            plano.insert(0, "Prosseguir para agendamento sem exames cardiovasculares de rotina")
            plano += [
                f"Classe ASA-PS provisória: {asa} (atribuição final é do anestesiologista)",
                "Encaminhar à consulta pré-anestésica",
            ]
            notas.append("Gate ESC (N3): < 65 anos, sem fatores de risco/doença CV, porte baixo/intermediário — liberado sem exames CV")
            return Resultado(
                saida="plano", asa=asa, asa_criterios=asa_criterios, porte=porte,
                sinalizadores=sinalizadores, exames=exames, plano=plano,
                notas=notas, trajeto=trajeto,
            )

        # ---------------- N6 — exames de entrada ----------------
        trajeto.append("N6")
        self._pede(r, "ecg_12m", "N6")
        self._pede(r, "anticoagulante", "N6")
        self._pede(r, "sopro_com_sintoma", "N6")
        self._pede(r, "sinais_ic", "N6")
        if r["diabetes"] != "nao":
            self._pede(r, "hba1c_3m", "N6")

        exames = avaliar_matriz(self.protocolo, r, asa, porte, idade)

        em_risco_esc = idade >= 65 or fatores_risco or doenca_cv
        if em_risco_esc and porte in ("intermediario", "alto"):
            reforcar(exames, "ecg_repouso", "sim", "Pacote de entrada ESC (≥65 anos ou fatores de risco/doença CV)")
            reforcar(exames, "nt_probnp_bnp", "sim", "Pacote de entrada ESC")
            if self.config["vigilancia_mins_ativa"]:
                reforcar(exames, "hs_ctn_basal", "sim", "Vigilância de MINS ativa (decisão editorial ESC, parametrizável)")
                plano.append("Vigilância de MINS: hs-cTn 24/48 h pós-operatório (registrar no plano cirúrgico)")
        elif idade >= 45 and porte == "alto":
            # Exceção ESC: adulto ≥45 anos sem fatores, cirurgia de alto risco
            reforcar(exames, "ecg_repouso", "considerar", "Exceção ESC: ≥ 45 anos + porte alto, mesmo sem fatores de risco")
            reforcar(exames, "nt_probnp_bnp", "considerar", "Exceção ESC: ≥ 45 anos + porte alto")
            notas.append("Exceção ESC aplicada: ≥ 45 anos + cirurgia de alto risco sem fatores de risco → considerar ECG + biomarcadores")

        # ---------------- N7 — refinamento por escore ----------------
        trajeto.append("N7")
        rcri = calcular_rcri(r, porte)

        # ---------------- N8/N9 — teste muda a conduta? / imagem de estresse ----------------
        trajeto.append("N8")
        if porte == "alto" and mets != "sim" and (rcri["escore"] >= 2 or r["hist_doenca_coronariana"]):
            trajeto.append("N9")
            exames["imagem_estresse"] = {
                "recomendacao": "considerar",
                "condicao": "Somente se o resultado mudar a conduta (nó N8) — porte alto + capacidade funcional ruim + probabilidade de DAC",
                "condicao_atendida": None,
            }

        # ---------------- N10 — alternativas não cirúrgicas ----------------
        fragilidade_avancada = frail is not None and frail >= 4
        risco_muito_alto = rcri["escore"] >= 3 and mets != "sim"
        if fragilidade_avancada or risco_muito_alto:
            trajeto.append("N10")
            motivo_n10 = "fragilidade avançada" if fragilidade_avancada else "risco cardiovascular muito alto com capacidade funcional ruim"
            sinalizadores.append({"id": "discutir_alternativas", "detalhe": motivo_n10})
            plano.append(
                "Conversa estruturada sobre alternativas não cirúrgicas, manejo conservador "
                f"ou cuidados paliativos ANTES do agendamento ({motivo_n10})"
            )

        # ---------------- N11 — decisão compartilhada e plano ----------------
        trajeto.append("N11")
        plano += [
            f"Classe ASA-PS provisória: {asa} (atribuição final é do anestesiologista)",
            f"RCRI {rcri['escore']} ponto(s) — risco estimado de evento cardíaco maior: {rcri['risco_estimado_evento_cardiaco_maior']}",
            "Consolidar decisão compartilhada: operar / otimizar e reavaliar / reconsiderar indicação",
            "Encaminhar à consulta pré-anestésica com a lista de exames gerada",
        ]
        if frail is not None and 3 <= frail < 4:
            plano.append("Avaliação geriátrica ampliada (FRAIL ≥ 3)")

        return Resultado(
            saida="plano", asa=asa, asa_criterios=asa_criterios, porte=porte,
            rcri=rcri, sinalizadores=sinalizadores, exames=exames,
            plano=plano, notas=notas, trajeto=trajeto,
        )
