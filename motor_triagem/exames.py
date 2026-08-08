"""Avaliador da matriz de exames NICE NG45 (módulo 'matriz_exames_nice').

Lê as regras diretamente do JSON do protocolo (data-driven) e, quando a
recomendação é 'considerar', tenta resolver a condição com o estado já
coletado. Se o estado não permite resolver, a condição fica registrada como
pendente ('condicao_atendida': None) para decisão da equipe.
"""

ORDEM_FORCA = {"nao": 0, "considerar": 1, "sim": 2}


def _contexto(r, idade):
    doenca_cv = bool(
        r.get("hist_doenca_coronariana")
        or r.get("hist_avc_ait")
        or r.get("insuficiencia_cardiaca_historia")
        or r.get("fe_reduzida") in ("moderada", "grave")
        or r.get("marcapasso")
    )
    doenca_renal = bool(r.get("doenca_renal_cronica") or r.get("dialise") not in (None, "nao"))
    return {
        "idade": idade,
        "doenca_cv": doenca_cv,
        "doenca_renal": doenca_renal,
        "diabetes": r.get("diabetes") not in (None, "nao"),
        "risco_lra": doenca_renal or r.get("diabetes") not in (None, "nao") or idade >= 65,
        "doenca_hepatica": bool(r.get("hepatite_ativa")),
        "ecg_12m": r.get("ecg_12m"),
    }


def _resolver_considerar(exame, porte, ctx):
    """Devolve True/False/None para a condição da célula 'considerar'."""
    if exame == "hemograma_completo":
        return ctx["doenca_cv"] or ctx["doenca_renal"]
    if exame == "funcao_renal_creatinina_eletrolitos":
        return ctx["risco_lra"]
    if exame == "ecg_repouso":
        if porte == "baixo":
            return None if ctx["ecg_12m"] is None else not ctx["ecg_12m"]
        if porte == "intermediario":
            return ctx["doenca_cv"] or ctx["doenca_renal"] or ctx["diabetes"]
        if porte == "alto":
            if ctx["idade"] <= 65:
                return False
            return None if ctx["ecg_12m"] is None else not ctx["ecg_12m"]
    if exame == "coagulograma_hemostasia":
        return ctx["doenca_hepatica"]
    return None


def avaliar_matriz(protocolo, r, asa, porte, idade):
    """Devolve {exame: {recomendacao, condicao, condicao_atendida}}."""
    ctx = _contexto(r, idade)
    matriz = protocolo["matriz_exames_nice"]
    resultado = {}

    for exame in matriz["exames_por_porte_e_asa"]:
        nome = exame["exame"]
        regra = next(
            (rg for rg in exame["regras"] if rg["porte"] == porte and asa in rg["asa"]),
            None,
        )
        if regra is None:
            continue
        item = {"recomendacao": regra["recomendacao"], "condicao": regra.get("condicao")}
        if regra["recomendacao"] == "considerar":
            item["condicao_atendida"] = _resolver_considerar(nome, porte, ctx)
        resultado[nome] = item

    # Exames com regra independente de porte × ASA
    resultado["radiografia_torax"] = {"recomendacao": "nao", "condicao": None}
    resultado["polissonografia"] = {"recomendacao": "nao", "condicao": None}
    resultado["eletroforese_falciforme"] = {"recomendacao": "nao", "condicao": None}
    resultado["urina_eas"] = {
        "recomendacao": "considerar",
        "condicao": "Urocultura apenas se infecção urinária mudaria a conduta",
        "condicao_atendida": None,
    }

    eco_atendida = None
    if r.get("sopro_com_sintoma") is not None or r.get("sinais_ic") is not None:
        eco_atendida = bool(r.get("sopro_com_sintoma")) or bool(r.get("sinais_ic"))
    resultado["ecocardiograma_repouso"] = {
        "recomendacao": "considerar",
        "condicao": "Sopro com sintoma cardíaco OU sinais de IC; fazer ECG antes e discutir com anestesiologista",
        "condicao_atendida": eco_atendida,
    }

    resultado["funcao_pulmonar_ou_gasometria"] = {
        "recomendacao": "considerar",
        "condicao": "ASA III–IV com doença respiratória, após parecer de anestesiologista sênior",
        "condicao_atendida": asa in ("III", "IV") and bool(r.get("dpoc") or r.get("doenca_pulmonar_leve")),
    }

    if ctx["diabetes"]:
        sem_recente = r.get("hba1c_3m") is False
        resultado["hba1c"] = {
            "recomendacao": "sim" if sem_recente else "considerar",
            "condicao": "Oferecer se não houver HbA1c dos últimos 3 meses",
            "condicao_atendida": sem_recente if r.get("hba1c_3m") is not None else None,
        }
    else:
        resultado["hba1c"] = {"recomendacao": "nao", "condicao": "Sem diagnóstico de diabetes"}

    gestacao = r.get("gestacao")
    if gestacao in ("duvida", "sim"):
        resultado["teste_gravidez"] = {
            "recomendacao": "sim",
            "condicao": "Oferecer com consentimento (possibilidade/confirmação de gestação)",
        }
    elif gestacao == "nao":
        resultado["teste_gravidez"] = {
            "recomendacao": "considerar",
            "condicao": "Reperguntar no dia do procedimento; oferecer se qualquer dúvida",
            "condicao_atendida": None,
        }
    else:
        resultado["teste_gravidez"] = {"recomendacao": "nao", "condicao": "Não se aplica"}

    if r.get("anticoagulante"):
        item = resultado.get("coagulograma_hemostasia", {"recomendacao": "nao", "condicao": None})
        item["nota"] = "Uso de anticoagulante: seguir via específica local (INR conforme protocolo)"
        resultado["coagulograma_hemostasia"] = item

    return resultado


def reforcar(resultado, exame, nivel, condicao=None):
    """Eleva a recomendação de um exame se 'nivel' for mais forte que a atual."""
    atual = resultado.get(exame)
    if atual is None or ORDEM_FORCA[nivel] > ORDEM_FORCA.get(atual["recomendacao"], 0):
        resultado[exame] = {"recomendacao": nivel, "condicao": condicao}
    return resultado
