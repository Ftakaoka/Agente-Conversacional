"""Travessia do grafo a partir de um paciente.

    Paciente -APRESENTA-> Achado -SUGERE-> Mecanismo <-CORRIGE- Intervenção
             <-TESTOU- Estudo -MEDIU-> Desfecho -CONTA_PARA-> CASA

Duas consultas sobre a mesma travessia:

  Q+  os caminhos que FECHAM até CASA        -> sobreviventes / condicionais
  Q-  os caminhos que QUEBRAM                -> cemitério, rotulado pela aresta
                                                que faltou (F1..F4)

Não há similaridade semântica em lugar nenhum: a recuperação é o caminho, e a
explicação é o caminho verbalizado.
"""

from dataclasses import dataclass, field

LAPIDES = {
    "F0": "Ninguém testou. Só existe a aresta de mecanismo.",
    "F1": "Foi testado — em outro paciente.",
    "F2": "Mediu desfecho substituto; não há caminho até CASA.",
    "F3": "Mediu desfecho duro e deu nulo (ou pior).",
    "F4": "O custo adverso consome o ganho.",
}


@dataclass
class Rota:
    """Um caminho completo, do achado ao (possível) nó CASA."""
    achado: str
    forca: str
    mecanismo: str
    plausibilidade: str
    intervencao: str
    estudo: str
    elegibilidade: object


@dataclass
class Veredito:
    intervencao: str
    estudo: str
    classe: str = "cemiterio"          # sobrevivente | condicional | cemiterio
    rota: Rota = None
    falhas: list = field(default_factory=list)      # [(codigo, motivo)]
    ressalvas: list = field(default_factory=list)
    medidas_duras: list = field(default_factory=list)
    medidas_substitutas: list = field(default_factory=list)
    adversos: list = field(default_factory=list)
    custos: list = field(default_factory=list)
    conflitos: list = field(default_factory=list)
    limites: list = field(default_factory=list)
    escore: int = 0


def _rotas(grafo, paciente):
    """Todas as rotas achado -> mecanismo -> intervenção -> estudo."""
    vistas = {}
    for id_achado in paciente["achados"]:
        for id_mec, forca in grafo.mecanismos_de(id_achado):
            for id_int, plaus in grafo.intervencoes_que_corrigem(id_mec):
                for estudo, _testou in grafo.estudos_que_testaram(id_int):
                    chave = (id_int, estudo["id"])
                    elig = grafo.elegibilidade(paciente, estudo)
                    rota = Rota(id_achado, forca, id_mec, plaus, id_int, estudo["id"], elig)
                    # guarda a rota de mecanismo mais forte para o mesmo par
                    anterior = vistas.get(chave)
                    if anterior is None or _peso(forca, plaus) > _peso(anterior.forca, anterior.plausibilidade):
                        vistas[chave] = rota
    return list(vistas.values())


_ESCALA = {"alta": 3, "media": 2, "baixa": 1}


def _peso(forca, plausibilidade):
    return _ESCALA.get(forca, 0) + _ESCALA.get(plausibilidade, 0)


def _julgar(grafo, rota):
    v = Veredito(intervencao=rota.intervencao, estudo=rota.estudo, rota=rota)
    intervencao = grafo.intervencoes[rota.intervencao]
    estudo = grafo.estudos[rota.estudo]
    desescalada = intervencao["logica_de_valor"] == "desescalada"

    for m in grafo.medidas_de(rota.estudo):
        tipo = grafo.desfechos[m["desfecho"]]["tipo"]
        if tipo == "duro":
            v.medidas_duras.append(m)
        elif tipo == "substituto":
            v.medidas_substitutas.append(m)
        else:
            v.adversos.append(m)
    v.custos = grafo.custos_de(rota.intervencao)
    v.conflitos = [c for c in grafo.conflita_com if rota.estudo in (c["a"], c["b"])]

    # F1 — a aresta ELEGIVEL não fecha
    if not rota.elegibilidade.elegivel:
        v.falhas.append(("F1", rota.elegibilidade.motivo))
        return v
    if rota.elegibilidade.estado == "transferivel":
        v.ressalvas.append(f"Elegibilidade por transferência, não direta: {rota.elegibilidade.motivo}")

    duros_primarios = [m for m in v.medidas_duras if m["primario"]]
    beneficio_primario = [m for m in duros_primarios if m["direcao"] == "beneficio"]
    ni_primario = [m for m in duros_primarios if m["direcao"] == "nao_inferior"]
    dano_duro = [m for m in v.medidas_duras if m["direcao"] == "dano"]
    beneficio_secundario = [m for m in v.medidas_duras if not m["primario"] and m["direcao"] == "beneficio"]
    subst_beneficio = [m for m in v.medidas_substitutas if m["direcao"] == "beneficio"]

    # F3 — mediu desfecho duro e foi PIOR
    if dano_duro:
        v.falhas.append(("F3", f"{estudo['rotulo']} mediu desfecho duro e o resultado foi dano: {dano_duro[0]['efeito']}"))
        return v

    # F2 — nenhum desfecho duro: o caminho morre no beco do substituto
    if not v.medidas_duras:
        alvo = v.medidas_substitutas[0]["desfecho"] if v.medidas_substitutas else "—"
        v.falhas.append(("F2", f"{estudo['rotulo']} só mediu desfecho substituto ({grafo.desfechos[alvo]['rotulo'] if alvo != '—' else '—'}); esse nó não tem aresta CONTA_PARA até CASA"))
        return v

    if beneficio_primario:
        v.classe = "sobrevivente"
        v.escore = 10
    elif ni_primario and desescalada:
        v.classe = "sobrevivente"
        v.escore = 9
        v.ressalvas.append("O ensaio demonstrou NÃO-INFERIORIDADE, não superioridade — e para uma intervenção de desescalada isso basta: o ganho está fora do desfecho (recurso escasso poupado, exposição evitada, custo zero).")
    elif ni_primario and subst_beneficio:
        v.classe = "condicional"
        v.escore = 6
        v.ressalvas.append("Segurança demonstrada em desfecho duro (não-inferioridade) e ganho apenas em desfecho substituto. Recomendável, mas o benefício em CASA não foi medido.")
    elif beneficio_secundario:
        v.classe = "condicional"
        v.escore = 4
        v.ressalvas.append(f"O desfecho primário duro foi nulo; o único caminho até CASA passa por desfecho SECUNDÁRIO ({grafo.desfechos[beneficio_secundario[0]['desfecho']]['rotulo']}) — gerador de hipótese, não prova.")
    else:
        nulo = duros_primarios[0] if duros_primarios else v.medidas_duras[0]
        v.falhas.append(("F3", f"{estudo['rotulo']} mediu o desfecho certo, no paciente certo, e o resultado foi nulo: {nulo['efeito']}"))
        return v

    # F4 — o contrapeso adverso
    danos = [m for m in v.adversos if m["direcao"] == "dano"]
    if danos:
        v.escore -= 2 * len(danos)
        for d in danos:
            v.ressalvas.append(f"Custo medido no mesmo ensaio: {grafo.desfechos[d['desfecho']]['rotulo']} — {d['efeito']}")
        if v.escore <= 3:
            v.classe = "cemiterio"
            v.falhas.append(("F4", "o custo adverso medido consome o ganho"))
            return v

    # co-primário que não fechou (o caso POISE-3)
    for m in duros_primarios:
        if m["direcao"] == "incerto":
            v.ressalvas.append(f"Co-primário não resolvido: {m['nota']}")
            v.escore -= 1

    if not intervencao["sus"]:
        v.escore -= 1
        v.ressalvas.append(f"Disponibilidade: {intervencao['rotulo']} é hemoderivado industrializado, {intervencao['custo_ordem']}, indisponível na maioria dos serviços públicos. Uma recomendação sobre insumo que não existe amplia desigualdade.")

    return v


def _sem_ensaio(grafo, paciente):
    """F0 — intervenções que o mecanismo alcança e que nenhum ensaio testou.

    Não é o mesmo que 'não funciona'. É que o grafo não tem como levá-las até
    CASA: a única aresta que as sustenta é CORRIGE, plausibilidade de
    mecanismo. É exatamente a posição de boa parte dos hemoderivados.
    """
    saida = []
    for id_achado in paciente["achados"]:
        for id_mec, forca in grafo.mecanismos_de(id_achado):
            for id_int, plaus in grafo.intervencoes_que_corrigem(id_mec):
                if grafo.estudos_que_testaram(id_int):
                    continue
                if any(v.intervencao == id_int for v in saida):
                    continue
                rota = Rota(id_achado, forca, id_mec, plaus, id_int, None, None)
                v = Veredito(intervencao=id_int, estudo=None, rota=rota)
                v.custos = grafo.custos_de(id_int)
                v.falhas.append((
                    "F0",
                    f"nenhum ensaio deste grafo testou {grafo.intervencoes[id_int]['rotulo'].lower()} "
                    f"contra comparador em desfecho duro nesta população; a única aresta que a sustenta "
                    f"é CORRIGE ({plaus} plausibilidade sobre {grafo.mecanismos[id_mec]['rotulo'].lower()})",
                ))
                saida.append(v)
    return saida


def navegar(grafo, id_paciente):
    """Executa Q+ e Q- para um paciente e devolve os vereditos ordenados."""
    paciente = grafo.pacientes[id_paciente]
    vereditos = [_julgar(grafo, r) for r in _rotas(grafo, paciente)]
    vereditos += _sem_ensaio(grafo, paciente)

    # estudos-limite viram advertência acoplada à mesma intervenção
    def _e_limite(v):
        return v.estudo is not None and grafo.estudos[v.estudo]["papel"] == "limite"

    limites = [v for v in vereditos if _e_limite(v)]
    vereditos = [v for v in vereditos if not _e_limite(v)]
    for v in vereditos:
        for lim in limites:
            if lim.intervencao == v.intervencao:
                v.limites.append(lim.estudo)

    sobreviventes = sorted([v for v in vereditos if v.classe == "sobrevivente"], key=lambda v: -v.escore)
    condicionais = sorted([v for v in vereditos if v.classe == "condicional"], key=lambda v: -v.escore)
    cemiterio = sorted([v for v in vereditos if v.classe == "cemiterio"], key=lambda v: v.falhas[0][0])
    return {
        "paciente": paciente,
        "sobreviventes": sobreviventes,
        "condicionais": condicionais,
        "cemiterio": cemiterio,
        "limites": limites,
    }
