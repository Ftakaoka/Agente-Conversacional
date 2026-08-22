"""CLI do grafo.

    python3 -m motor_grafo                # lista os pacientes
    python3 -m motor_grafo P1             # navega um paciente
    python3 -m motor_grafo --todos        # os três, em sequência (modo palco)
    python3 -m motor_grafo --json P1      # saída estruturada
"""

import json
import sys

from .grafo import Grafo
from .travessia import navegar
from .explicacao import relatorio, explicar


def _serializar(grafo, resultado):
    def v2d(v):
        titulo, linhas = explicar(grafo, v)
        return {"intervencao": v.intervencao, "estudo": v.estudo, "classe": v.classe,
                "escore": v.escore, "titulo": titulo, "trajeto": linhas,
                "falhas": [{"codigo": c, "motivo": m} for c, m in v.falhas]}
    return {"paciente": resultado["paciente"],
            "sobreviventes": [v2d(v) for v in resultado["sobreviventes"]],
            "condicionais": [v2d(v) for v in resultado["condicionais"]],
            "cemiterio": [v2d(v) for v in resultado["cemiterio"]]}


def main(argv):
    grafo = Grafo()
    args = [a for a in argv if not a.startswith("--")]
    flags = {a for a in argv if a.startswith("--")}

    if "--todos" in flags:
        alvos = list(grafo.pacientes)
    elif args:
        alvos = args
    else:
        print("Pacientes disponíveis:\n")
        for p in grafo.pacientes.values():
            print(f"  {p['id']}  {p['nome']} — {p['caso']}")
        print("\nUso: python3 -m motor_grafo P1 | --todos | --json P1")
        return 0

    saidas = []
    for pid in alvos:
        if pid not in grafo.pacientes:
            print(f"Paciente desconhecido: {pid}", file=sys.stderr)
            return 1
        resultado = navegar(grafo, pid)
        if "--json" in flags:
            saidas.append(_serializar(grafo, resultado))
        else:
            print(relatorio(grafo, resultado))
            print()
    if "--json" in flags:
        print(json.dumps(saidas, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
