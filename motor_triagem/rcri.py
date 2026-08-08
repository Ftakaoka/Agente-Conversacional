"""Escore RCRI (Revised Cardiac Risk Index) — nó N7, enxerto ACC/AHA 2024.

Aproximações declaradas: 'cirurgia de alto risco RCRI' é aproximada pelo porte
ESC alto; 'creatinina > 2 mg/dL' é aproximada por doença renal em diálise ou
DRC diagnosticada.
"""

RISCO_POR_ESCORE = {0: "0,4%", 1: "0,9%", 2: "6,6%"}


def calcular_rcri(r, porte):
    componentes = []
    if porte == "alto":
        componentes.append("Cirurgia de alto risco (aproximada pelo porte ESC alto)")
    if r.get("hist_doenca_coronariana"):
        componentes.append("Doença isquêmica do coração")
    if r.get("insuficiencia_cardiaca_historia"):
        componentes.append("História de insuficiência cardíaca")
    if r.get("hist_avc_ait"):
        componentes.append("Doença cerebrovascular (AVC/AIT)")
    if r.get("diabetes_insulina"):
        componentes.append("Diabetes em uso de insulina")
    if r.get("dialise") not in (None, "nao") or r.get("doenca_renal_cronica"):
        componentes.append("Creatinina > 2 mg/dL (aproximada por doença renal)")

    escore = len(componentes)
    return {
        "escore": escore,
        "componentes": componentes,
        "risco_estimado_evento_cardiaco_maior": RISCO_POR_ESCORE.get(escore, "≥ 11%"),
        "classe_risco": "baixo" if escore <= 1 else ("elevado" if escore == 2 else "alto"),
    }
