"""Classificador ASA-PS provisório (módulo 'classificador_asa_ps' do protocolo).

Percorre os passos na ordem do protocolo: primeiro os critérios de ASA IV,
depois III, depois II; sem critério satisfeito → ASA I. Classes V e VI não
ocorrem em fluxo eletivo de contemplação e não são geradas aqui.
"""


def classificar_asa(r):
    """Recebe o dicionário de respostas e devolve (classe, criterios_atendidos)."""
    iv = []
    if r.get("evento_timing") == "menos_3_meses":
        iv.append("IAM/AVC/AIT/stent há menos de 3 meses")
    if r.get("fe_reduzida") == "grave":
        iv.append("Redução grave da fração de ejeção")
    if r.get("dialise") == "indicada_sem_realizar":
        iv.append("Doença renal terminal sem diálise regular")
    if iv:
        return "IV", iv

    iii = []
    if r.get("diabetes") == "mal_controlado":
        iii.append("Diabetes mal controlado")
    if r.get("hipertensao") == "mal_controlada":
        iii.append("Hipertensão mal controlada")
    if r.get("dpoc"):
        iii.append("DPOC / doença pulmonar moderada a grave")
    if (r.get("imc") or 0) >= 40:
        iii.append("IMC ≥ 40")
    if r.get("hepatite_ativa"):
        iii.append("Hepatite ativa / doença hepática crônica")
    if r.get("alcool") == "dependencia":
        iii.append("Dependência ou abuso de álcool")
    if r.get("marcapasso"):
        iii.append("Marca-passo implantado")
    if r.get("fe_reduzida") == "moderada":
        iii.append("Redução moderada da fração de ejeção")
    if r.get("dialise") == "regular":
        iii.append("Doença renal terminal em diálise regular")
    if r.get("evento_timing") == "3_meses_ou_mais":
        iii.append("IAM/AVC/AIT/stent há mais de 3 meses")
    if r.get("insuficiencia_cardiaca_historia"):
        iii.append("Insuficiência cardíaca diagnosticada")
    if r.get("limitacao_funcional_substantiva"):
        iii.append("Limitação funcional substantiva por doença")
    if r.get("outra_doenca") == "grave":
        iii.append("Outra doença moderada a grave")
    if iii:
        return "III", iii

    ii = []
    if r.get("tabagismo_atual"):
        ii.append("Tabagismo atual")
    if r.get("alcool") == "social":
        ii.append("Etilismo social")
    if r.get("gestacao") == "sim":
        ii.append("Gestação")
    if 30 <= (r.get("imc") or 0) < 40:
        ii.append("Obesidade (30 ≤ IMC < 40)")
    if r.get("diabetes") == "bem_controlado":
        ii.append("Diabetes bem controlado")
    if r.get("hipertensao") == "bem_controlada":
        ii.append("Hipertensão bem controlada")
    if r.get("doenca_pulmonar_leve"):
        ii.append("Doença pulmonar leve")
    if r.get("doenca_renal_cronica"):
        ii.append("Doença renal crônica sem diálise (aproximado como leve; revisar estágio)")
    if r.get("outra_doenca") == "leve":
        ii.append("Outra doença leve")
    if ii:
        return "II", ii

    return "I", ["Saudável, sem doença sistêmica"]
