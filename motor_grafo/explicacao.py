"""Verbalização do caminho em PT-BR.

A explicação não é gerada por um modelo de linguagem: ela é o caminho lido em
voz alta, aresta por aresta. Toda frase abaixo corresponde a uma aresta do
grafo — se a frase existe, a aresta existe.
"""

from .travessia import LAPIDES

ARTIGO = {"alta": "alta", "media": "média", "baixa": "baixa"}
DIRECAO = {
    "beneficio": "benefício",
    "nulo": "nulo",
    "nao_inferior": "não-inferioridade",
    "incerto": "incerto",
    "dano": "dano",
}


def _n(grafo, tipo, id_):
    return grafo.bruto and {
        "achado": grafo.achados, "mecanismo": grafo.mecanismos,
        "intervencao": grafo.intervencoes, "desfecho": grafo.desfechos,
        "estudo": grafo.estudos,
    }[tipo][id_]["rotulo"]


def explicar(grafo, veredito):
    """Devolve (titulo, linhas[]) — o trajeto verbalizado."""
    intervencao = grafo.intervencoes[veredito.intervencao]
    r = veredito.rota
    linhas = []

    if veredito.estudo is None:                       # F0
        linhas.append(f"APRESENTA → {_n(grafo,'achado',r.achado)}")
        linhas.append(f"SUGERE ({ARTIGO[r.forca]}) → {_n(grafo,'mecanismo',r.mecanismo)}")
        linhas.append(f"CORRIGE ({ARTIGO[r.plausibilidade]} plausibilidade) ← {intervencao['rotulo']}")
        linhas.append("TESTOU → a aresta não existe. O caminho termina aqui.")
        linhas.append(f"⛔ F0: {veredito.falhas[0][1]}.")
        linhas.append(f"⚑ {LAPIDES['F0']}")
        linhas.append("Isto não prova que não funciona. Prova que o grafo não tem como levá-la até CASA.")
        return f"{intervencao['rotulo']} — {LAPIDES['F0']}", linhas

    estudo = grafo.estudos[veredito.estudo]
    linhas.append(f"APRESENTA → {_n(grafo,'achado',r.achado)}")
    linhas.append(f"SUGERE ({ARTIGO[r.forca]}) → {_n(grafo,'mecanismo',r.mecanismo)}")
    linhas.append(f"CORRIGE ({ARTIGO[r.plausibilidade]} plausibilidade) ← {intervencao['rotulo']}")
    linhas.append(f"TESTOU ← {estudo['rotulo']} ({estudo['ano']}, n={estudo['n'] or 's/n'})")

    codigos = [c for c, _ in veredito.falhas]

    if "F1" in codigos:
        linhas.append(f"ELEGIVEL → ⛔ quebra: {dict(veredito.falhas)['F1']}.")
        linhas.append(f"⚑ {LAPIDES['F1']}")
        return f"{intervencao['rotulo']} × {estudo['rotulo']}", linhas

    linhas.append(f"ELEGIVEL ({r.elegibilidade.estado}) → {r.elegibilidade.motivo}")

    for m in veredito.medidas_duras + veredito.medidas_substitutas + veredito.adversos:
        tipo = grafo.desfechos[m["desfecho"]]["tipo"]
        marca = {"duro": "●", "substituto": "○", "adverso": "▲"}[tipo]
        primario = "primário" if m["primario"] else "secundário"
        ic = f" [IC 95% {m['ic']}]" if m["ic"] not in ("—", "", None) else ""
        linhas.append(
            f"MEDIU {marca} {_n(grafo,'desfecho',m['desfecho'])} "
            f"({tipo}, {primario}, {DIRECAO[m['direcao']]}): {m['efeito']}{ic}"
        )
        if tipo == "substituto":
            linhas.append("   └─ CONTA_PARA → ⛔ desfecho substituto não tem aresta até CASA.")
        else:
            linhas.append(f"   └─ CONTA_PARA ({grafo.conta_para[m['desfecho']]}) → CASA")

    for codigo, motivo in veredito.falhas:
        if codigo != "F1":
            linhas.append(f"⛔ {codigo}: {motivo}.")
            linhas.append(f"⚑ {LAPIDES[codigo]}")

    for res in veredito.ressalvas:
        linhas.append(f"⚠ {res}")

    for c in veredito.custos:
        if c["fonte"] != veredito.estudo:
            linhas.append(
                f"CUSTA ▲ {_n(grafo,'desfecho',c['desfecho'])}: {c['efeito']} "
                f"— observado em OUTRA população ({c['fonte']}); transposição incerta, mas é o contrapeso conhecido."
            )

    for lim in veredito.limites:
        e = grafo.estudos[lim]
        linhas.append(f"LIMITE — {e['rotulo']}: {e['populacao']['transferivel_para'][0]['ressalva']}")

    for cf in veredito.conflitos:
        outro = cf["b"] if cf["a"] == veredito.estudo else cf["a"]
        linhas.append(f"CONFLITA_COM {grafo.estudos[outro]['rotulo']} — {cf['eixo']}")

    if intervencao["janela_h"]:
        linhas.append(
            f"JANELA — em {intervencao.get('janela_contexto', 'hemorragia aguda')} o efeito é dependente do tempo "
            f"(< {intervencao['janela_h']} h). Em cirurgia eletiva a administração é programada: a janela deixa de "
            f"ser o fator limitante, e o que resta é a dose e a indicação."
        )

    return f"{intervencao['rotulo']} × {estudo['rotulo']}", linhas


def relatorio(grafo, resultado):
    """Relatório completo de um paciente, em texto."""
    p = resultado["paciente"]
    out = []
    out.append("=" * 78)
    out.append(f"PACIENTE {p['id']} — {p['nome']}")
    out.append(p["caso"])
    out.append(f'META (nó CASA): "{p["meta"]}"')
    out.append("=" * 78)

    for rotulo, chave in (("SOBREVIVEM — caminho fechado até CASA", "sobreviventes"),
                          ("CONDICIONAIS — caminho fecha, mas frágil", "condicionais"),
                          ("CEMITÉRIO — o caminho quebra", "cemiterio")):
        out.append("")
        out.append(f"### {rotulo}  ({len(resultado[chave])})")
        if not resultado[chave]:
            out.append("   (nenhum)")
        for v in resultado[chave]:
            titulo, linhas = explicar(grafo, v)
            out.append("")
            marca = {"sobrevivente": "✔", "condicional": "~", "cemiterio": "✖"}[v.classe]
            out.append(f" {marca} {titulo}")
            for l in linhas:
                out.append(f"      {l}")
    out.append("")
    out.append("-" * 78)
    out.append("Arestas de evidência: auditado=false. Conferir contra o artigo primário "
               "antes de uso público (grafos/AUDITORIA.md).")
    return "\n".join(out)
