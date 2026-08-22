"""Gera o artefato de palco a partir do grafo e do motor.

    python3 grafos/exportar_palco.py [saida.html]

A página é autocontida: o payload é a saída do próprio motor de travessia,
embutida no HTML. Regerar depois de qualquer mudança no grafo — inclusive
depois de auditar as arestas de evidência.
"""

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from motor_grafo import Grafo, navegar, explicar

RAIZ = pathlib.Path(__file__).resolve().parent
TEMPLATE = RAIZ / "palco.template.html"
PADRAO = RAIZ / "palco.html"


def payload(grafo):
    dados = {
        "meta": {
            "tese": grafo.meta["tese"],
            "lapides": {m["id"]: m["lapide"] for m in grafo.meta["modos_de_falha"]},
        },
        "nos": {
            "achado": {k: v["rotulo"] for k, v in grafo.achados.items()},
            "mecanismo": {k: v["rotulo"] for k, v in grafo.mecanismos.items()},
            "intervencao": {k: {"rotulo": v["rotulo"], "classe": v["classe"],
                                "sus": v["sus"], "custo": v["custo_ordem"]}
                            for k, v in grafo.intervencoes.items()},
            "estudo": {k: {"rotulo": v["rotulo"], "ano": v["ano"], "n": v["n"]}
                       for k, v in grafo.estudos.items()},
            "desfecho": {k: {"rotulo": v["rotulo"], "tipo": v["tipo"]}
                         for k, v in grafo.desfechos.items()},
        },
        "pacientes": [],
    }
    for pid in grafo.pacientes:
        resultado = navegar(grafo, pid)
        p = dict(resultado["paciente"])
        vereditos = []
        for grupo in ("sobreviventes", "condicionais", "cemiterio"):
            for v in resultado[grupo]:
                titulo, linhas = explicar(grafo, v)
                desfechos = [m["desfecho"] for m in v.medidas_duras + v.medidas_substitutas]
                vereditos.append({
                    "classe": v.classe, "titulo": titulo, "escore": v.escore,
                    "intervencao": v.intervencao, "estudo": v.estudo,
                    "achado": v.rota.achado, "mecanismo": v.rota.mecanismo,
                    "desfechos": desfechos,
                    "chegaCasa": v.classe != "cemiterio" and any(grafo.chega_em_casa(d) for d in desfechos),
                    "falha": v.falhas[0][0] if v.falhas else None,
                    "motivo": v.falhas[0][1] if v.falhas else None,
                    "trajeto": linhas,
                })
        p["vereditos"] = vereditos
        dados["pacientes"].append(p)
    return dados


def main(argv):
    saida = pathlib.Path(argv[0]) if argv else PADRAO
    grafo = Grafo()
    dados = json.dumps(payload(grafo), ensure_ascii=False, separators=(",", ":"))
    if "</script" in dados:
        raise SystemExit("payload contém '</script'; escapar antes de embutir")
    html = TEMPLATE.read_text(encoding="utf-8").replace("__PAYLOAD__", dados)
    saida.write_text(html, encoding="utf-8")
    total = sum(len(p["vereditos"]) for p in payload(grafo)["pacientes"])
    print(f"{saida}: {saida.stat().st_size} bytes, "
          f"{len(dados['pacientes']) if isinstance(dados, dict) else len(grafo.pacientes)} pacientes, {total} rotas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
