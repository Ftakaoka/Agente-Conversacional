"""Catálogo de variáveis de entrada do motor.

Cada variável tem o texto de pergunta (voltado à equipe/camada conversacional,
que pode humanizá-lo), o tipo e, quando enum, as opções (valor, rótulo).
"""

VARIAVEIS = {
    # N0 — contexto
    "idade": {
        "texto": "Qual é a idade do paciente (anos)?",
        "tipo": "numero",
    },
    "cirurgia_eletiva": {
        "texto": "A cirurgia em avaliação é eletiva (programada, sem urgência)?",
        "tipo": "booleano",
    },
    # N1 — instabilidade cardíaca
    "sca_recente": {
        "texto": "Há suspeita ou diagnóstico de síndrome coronariana aguda recente (dor torácica cardíaca em investigação ou infarto em curso)?",
        "tipo": "booleano",
    },
    "ic_descompensada": {
        "texto": "Há sinais de insuficiência cardíaca descompensada (falta de ar em repouso ou aos mínimos esforços, inchaço progressivo, ortopneia)?",
        "tipo": "booleano",
    },
    "arritmia_grave": {
        "texto": "Há arritmia grave conhecida ou suspeita (síncope, palpitações com desmaio, arritmia em tratamento instável)?",
        "tipo": "booleano",
    },
    "valvopatia_grave_sintomatica": {
        "texto": "Há doença valvar cardíaca grave e sintomática (estenose aórtica/mitral grave com sintomas)?",
        "tipo": "booleano",
    },
    # N2 — porte
    "procedimento": {
        "texto": "Qual é o procedimento cirúrgico proposto?",
        "tipo": "texto",
    },
    "porte": {
        "texto": "Não reconheci o procedimento. Qual é o porte/risco cardiovascular da cirurgia (tabela ESC 2022)?",
        "tipo": "enum",
        "opcoes": [
            ("baixo", "Baixo — risco de morte CV/IAM em 30 dias < 1% (ex.: superficial, mama, oftalmológica)"),
            ("intermediario", "Intermediário — risco 1–5% (ex.: intraperitoneal, ortopédica maior, cabeça e pescoço)"),
            ("alto", "Alto — risco > 5% (ex.: aórtica, vascular maior, pâncreas, esôfago, pneumectomia)"),
        ],
    },
    # N2b — anamnese para ASA-PS
    "hist_doenca_coronariana": {
        "texto": "O paciente já teve infarto, angioplastia com stent, cirurgia de ponte de safena ou angina diagnosticada?",
        "tipo": "booleano",
    },
    "hist_avc_ait": {
        "texto": "O paciente já teve AVC (derrame) ou AIT (isquemia cerebral transitória)?",
        "tipo": "booleano",
    },
    "evento_timing": {
        "texto": "O evento cardiovascular mais recente (infarto, stent, AVC ou AIT) ocorreu há quanto tempo?",
        "tipo": "enum",
        "opcoes": [
            ("menos_3_meses", "Há menos de 3 meses"),
            ("3_meses_ou_mais", "Há 3 meses ou mais"),
        ],
    },
    "insuficiencia_cardiaca_historia": {
        "texto": "O paciente tem diagnóstico de insuficiência cardíaca (mesmo que compensada)?",
        "tipo": "booleano",
    },
    "fe_reduzida": {
        "texto": "Há redução conhecida da fração de ejeção (força do coração) em ecocardiograma prévio?",
        "tipo": "enum",
        "opcoes": [
            ("nao", "Não / fração de ejeção normal"),
            ("moderada", "Redução moderada"),
            ("grave", "Redução grave"),
            ("nao_sei", "Não sei / nunca fez ecocardiograma"),
        ],
    },
    "marcapasso": {
        "texto": "O paciente tem marca-passo ou outro dispositivo cardíaco implantado?",
        "tipo": "booleano",
    },
    "dialise": {
        "texto": "O paciente faz diálise?",
        "tipo": "enum",
        "opcoes": [
            ("nao", "Não"),
            ("regular", "Sim, em programa regular"),
            ("indicada_sem_realizar", "Diálise indicada, mas não realizada regularmente"),
        ],
    },
    "doenca_renal_cronica": {
        "texto": "O paciente tem doença renal crônica diagnosticada (sem diálise)?",
        "tipo": "booleano",
    },
    "diabetes": {
        "texto": "O paciente tem diabetes?",
        "tipo": "enum",
        "opcoes": [
            ("nao", "Não"),
            ("bem_controlado", "Sim, bem controlado"),
            ("mal_controlado", "Sim, mal controlado"),
        ],
    },
    "diabetes_insulina": {
        "texto": "O diabetes é tratado com insulina?",
        "tipo": "booleano",
    },
    "hipertensao": {
        "texto": "O paciente tem pressão alta (hipertensão)?",
        "tipo": "enum",
        "opcoes": [
            ("nao", "Não"),
            ("bem_controlada", "Sim, bem controlada"),
            ("mal_controlada", "Sim, mal controlada"),
        ],
    },
    "dpoc": {
        "texto": "O paciente tem DPOC (enfisema/bronquite crônica) ou outra doença pulmonar moderada a grave?",
        "tipo": "booleano",
    },
    "doenca_pulmonar_leve": {
        "texto": "O paciente tem doença pulmonar leve (ex.: asma leve controlada)?",
        "tipo": "booleano",
    },
    "hepatite_ativa": {
        "texto": "O paciente tem hepatite ativa ou doença hepática crônica?",
        "tipo": "booleano",
    },
    "alcool": {
        "texto": "Como é o uso de bebida alcoólica?",
        "tipo": "enum",
        "opcoes": [
            ("ausente_minimo", "Não bebe ou uso mínimo"),
            ("social", "Uso social"),
            ("dependencia", "Uso pesado ou dependência"),
        ],
    },
    "tabagismo_atual": {
        "texto": "O paciente fuma atualmente?",
        "tipo": "booleano",
    },
    "imc": {
        "texto": "Qual é o IMC do paciente (kg/m²)? Se não souber, calcule: peso ÷ altura².",
        "tipo": "numero",
    },
    "gestacao": {
        "texto": "Há gestação em curso ou possibilidade de gestação?",
        "tipo": "enum",
        "opcoes": [
            ("nao_se_aplica", "Não se aplica"),
            ("nao", "Não"),
            ("duvida", "Possível / não tenho certeza"),
            ("sim", "Sim, gestação confirmada"),
        ],
    },
    "limitacao_funcional_substantiva": {
        "texto": "Alguma doença limita de forma importante as atividades do dia a dia do paciente?",
        "tipo": "booleano",
    },
    "outra_doenca": {
        "texto": "Há alguma outra doença relevante não citada até aqui?",
        "tipo": "enum",
        "opcoes": [
            ("nenhuma", "Nenhuma"),
            ("leve", "Sim, leve e controlada"),
            ("grave", "Sim, moderada a grave"),
        ],
    },
    # N4 — fragilidade
    "frail_score": {
        "texto": "Escore FRAIL (0–5): fadiga, resistência, deambulação, comorbidades ≥5, perda de peso >5%. Quantos itens positivos?",
        "tipo": "numero",
    },
    # N5 — capacidade funcional
    "mets_4": {
        "texto": "O paciente consegue subir dois lances de escada sem parar (≈ 4 METs)?",
        "tipo": "enum",
        "opcoes": [
            ("sim", "Sim"),
            ("nao", "Não"),
            ("nao_sei", "Não sei / indeterminado"),
        ],
    },
    # N6 — condições da matriz de exames
    "ecg_12m": {
        "texto": "O paciente tem ECG realizado nos últimos 12 meses?",
        "tipo": "booleano",
    },
    "anticoagulante": {
        "texto": "O paciente usa anticoagulante (varfarina, DOAC)?",
        "tipo": "booleano",
    },
    "sopro_com_sintoma": {
        "texto": "Há sopro cardíaco conhecido ACOMPANHADO de sintoma (falta de ar, desmaio, dor no peito)?",
        "tipo": "booleano",
    },
    "sinais_ic": {
        "texto": "Há sinais ou sintomas atuais de insuficiência cardíaca (fora de descompensação aguda)?",
        "tipo": "booleano",
    },
    "hba1c_3m": {
        "texto": "Há resultado de hemoglobina glicada (HbA1c) dos últimos 3 meses?",
        "tipo": "booleano",
    },
}
