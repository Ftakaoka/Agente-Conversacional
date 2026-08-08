"""CLI do motor de triagem.

Modo interativo (padrão):  python -m motor_triagem
Modo demonstração:         python -m motor_triagem --demo
"""

import sys

from .motor import Motor, Pergunta, Resultado, Sessao


def _imprimir_resultado(res: Resultado):
    print("\n" + "=" * 62)
    print(f"SAÍDA: {res.saida.upper()}")
    if res.motivo:
        print(f"Motivo: {res.motivo}")
    if res.asa:
        print(f"ASA-PS provisória: {res.asa}  ({'; '.join(res.asa_criterios)})")
    if res.porte:
        print(f"Porte cirúrgico (ESC): {res.porte}")
    if res.rcri:
        print(f"RCRI: {res.rcri['escore']} ponto(s) — risco {res.rcri['risco_estimado_evento_cardiaco_maior']}")
        for c in res.rcri["componentes"]:
            print(f"   • {c}")
    if res.sinalizadores:
        print("Sinalizadores:")
        for s in res.sinalizadores:
            print(f"   ⚑ {s['id']}: {s['detalhe']}")
    if res.exames:
        print("Exames:")
        for nome, item in sorted(res.exames.items()):
            linha = f"   [{item['recomendacao'].upper():10s}] {nome}"
            if item.get("condicao"):
                atendida = item.get("condicao_atendida")
                marca = {True: " (condição ATENDIDA)", False: " (condição não atendida)", None: " (condição a verificar)"}[atendida] if item["recomendacao"] == "considerar" else ""
                linha += f" — {item['condicao']}{marca}"
            if item.get("nota"):
                linha += f" | {item['nota']}"
            print(linha)
    if res.plano:
        print("Plano:")
        for p in res.plano:
            print(f"   → {p}")
    if res.notas:
        print("Notas:")
        for n in res.notas:
            print(f"   · {n}")
    print(f"Trajeto: {' → '.join(res.trajeto)}")
    print("=" * 62)


def _perguntar_no_terminal(p: Pergunta):
    print(f"\n[{p.no}] {p.texto}")
    if p.tipo == "booleano":
        while True:
            v = input("   (s/n) > ").strip().lower()
            if v in ("s", "sim"):
                return True
            if v in ("n", "nao", "não"):
                return False
    if p.tipo == "enum":
        for i, (_, rotulo) in enumerate(p.opcoes, 1):
            print(f"   {i}. {rotulo}")
        while True:
            v = input("   (número) > ").strip()
            if v.isdigit() and 1 <= int(v) <= len(p.opcoes):
                return p.opcoes[int(v) - 1][0]
    if p.tipo == "numero":
        while True:
            v = input("   (número) > ").strip().replace(",", ".")
            try:
                return float(v)
            except ValueError:
                pass
    return input("   > ").strip()


def executar_cenario(motor: Motor, respostas: dict) -> Resultado:
    """Percorre o fluxo respondendo a partir de um dicionário pronto."""
    sessao = Sessao()
    while True:
        passo = motor.avaliar(sessao)
        if isinstance(passo, Resultado):
            return passo
        if passo.id not in respostas:
            raise KeyError(f"Cenário não define a variável pedida: {passo.id}")
        sessao.responder(passo.id, respostas[passo.id])


CENARIOS = {
    "Jovem saudável — catarata": {
        "idade": 34, "cirurgia_eletiva": True,
        "sca_recente": False, "ic_descompensada": False,
        "arritmia_grave": False, "valvopatia_grave_sintomatica": False,
        "procedimento": "cirurgia de catarata",
        "hist_doenca_coronariana": False, "hist_avc_ait": False,
        "insuficiencia_cardiaca_historia": False, "fe_reduzida": "nao_sei",
        "marcapasso": False, "dialise": "nao", "doenca_renal_cronica": False,
        "diabetes": "nao", "hipertensao": "nao", "dpoc": False,
        "doenca_pulmonar_leve": False, "hepatite_ativa": False,
        "alcool": "ausente_minimo", "tabagismo_atual": False, "imc": 24,
        "gestacao": "nao_se_aplica", "limitacao_funcional_substantiva": False,
        "outra_doenca": "nenhuma", "mets_4": "sim",
    },
    "Idoso de risco — cirurgia de aorta": {
        "idade": 72, "cirurgia_eletiva": True,
        "sca_recente": False, "ic_descompensada": False,
        "arritmia_grave": False, "valvopatia_grave_sintomatica": False,
        "procedimento": "correção de aneurisma de aorta abdominal",
        "hist_doenca_coronariana": True, "hist_avc_ait": False,
        "evento_timing": "3_meses_ou_mais",
        "insuficiencia_cardiaca_historia": False, "fe_reduzida": "nao",
        "marcapasso": False, "dialise": "nao", "doenca_renal_cronica": False,
        "diabetes": "mal_controlado", "diabetes_insulina": True,
        "hipertensao": "mal_controlada", "dpoc": False,
        "doenca_pulmonar_leve": False, "hepatite_ativa": False,
        "alcool": "ausente_minimo", "tabagismo_atual": True, "imc": 29,
        "gestacao": "nao_se_aplica", "limitacao_funcional_substantiva": False,
        "outra_doenca": "nenhuma", "frail_score": 2, "mets_4": "nao",
        "ecg_12m": False, "anticoagulante": False,
        "sopro_com_sintoma": False, "sinais_ic": False, "hba1c_3m": False,
    },
    "Instável — IC descompensada": {
        "idade": 58, "cirurgia_eletiva": True,
        "sca_recente": False, "ic_descompensada": True,
    },
}


def main():
    motor = Motor()
    if "--demo" in sys.argv:
        for nome, respostas in CENARIOS.items():
            print(f"\n### CENÁRIO: {nome}")
            _imprimir_resultado(executar_cenario(motor, respostas))
        return
    print("Triagem pré-operatória — Vera PreOp.AI (protocolo híbrido ESC/ACC-AHA + ASA + NICE)")
    sessao = Sessao()
    while True:
        passo = motor.avaliar(sessao)
        if isinstance(passo, Resultado):
            _imprimir_resultado(passo)
            return
        sessao.responder(passo.id, _perguntar_no_terminal(passo))


if __name__ == "__main__":
    main()
