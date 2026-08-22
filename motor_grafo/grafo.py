"""Carga e indexação do grafo de hemostasia/PBM.

O grafo é dado, não código: `grafos/hemostasia-pbm.json`. Este módulo só o
carrega, indexa por id e resolve a única aresta que não está no arquivo —
ELEGIVEL, que é computada em tempo de consulta entre um paciente e um estudo.
"""

import json
from dataclasses import dataclass
from pathlib import Path

CAMINHO_GRAFO = Path(__file__).resolve().parent.parent / "grafos" / "hemostasia-pbm.json"


@dataclass
class Elegibilidade:
    estado: str          # 'direta' | 'transferivel' | 'inelegivel'
    motivo: str

    @property
    def elegivel(self):
        return self.estado in ("direta", "transferivel")


class Grafo:
    def __init__(self, caminho=CAMINHO_GRAFO):
        self.bruto = json.loads(Path(caminho).read_text(encoding="utf-8"))
        self.meta = self.bruto["meta"]
        self.terminal = self.bruto["terminal"]
        self.achados = self._indexar("achados")
        self.mecanismos = self._indexar("mecanismos")
        self.intervencoes = self._indexar("intervencoes")
        self.desfechos = self._indexar("desfechos")
        self.estudos = self._indexar("estudos")
        self.pacientes = self._indexar("pacientes")
        self.conta_para = {c["de"]: c["sinal"] for c in self.bruto["conta_para"]}
        self.sugere = self.bruto["sugere"]
        self.corrige = self.bruto["corrige"]
        self.mediu = self.bruto["mediu"]
        self.custa = self.bruto["custa"]
        self.conflita_com = self.bruto["conflita_com"]

    def _indexar(self, chave):
        return {n["id"]: n for n in self.bruto[chave]}

    # -- travessias elementares ------------------------------------------

    def mecanismos_de(self, id_achado):
        return [(a["para"], a["forca"]) for a in self.sugere if a["de"] == id_achado]

    def intervencoes_que_corrigem(self, id_mecanismo):
        return [(a["de"], a["plausibilidade"]) for a in self.corrige if a["para"] == id_mecanismo]

    def estudos_que_testaram(self, id_intervencao):
        saida = []
        for e in self.estudos.values():
            for t in e["testou"]:
                if t["intervencao"] == id_intervencao:
                    saida.append((e, t))
        return saida

    def medidas_de(self, id_estudo):
        return [m for m in self.mediu if m["estudo"] == id_estudo]

    def custos_de(self, id_intervencao):
        return [c for c in self.custa if c["intervencao"] == id_intervencao]

    def chega_em_casa(self, id_desfecho):
        """A aresta CONTA_PARA existe? Só desfecho duro (ou adverso, com sinal
        negativo) alcança o nó terminal. Substituto é beco sem saída."""
        return self.conta_para.get(id_desfecho)

    # -- a aresta computada ----------------------------------------------

    def elegibilidade(self, paciente, estudo):
        pop = estudo["populacao"]
        contextos = set(paciente["contextos"])
        exigidos = set(pop["contextos"])
        if contextos & exigidos:
            return Elegibilidade("direta", f"o paciente está em {sorted(contextos & exigidos)[0]}, contexto recrutado pelo ensaio")
        for t in pop.get("transferivel_para", []):
            if t["contexto"] in contextos:
                return Elegibilidade("transferivel", t["ressalva"])
        return Elegibilidade(
            "inelegivel",
            f"o ensaio recrutou {pop['descricao'].lower()}; este paciente não pertence a essa população",
        )
