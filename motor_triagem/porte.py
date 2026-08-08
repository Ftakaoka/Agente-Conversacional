"""Lookup de porte cirúrgico (módulo 'porte_cirurgico' do protocolo).

Classificação aproximada pela tabela ESC 2022 a partir de palavras-chave no
nome do procedimento. Se nenhuma palavra-chave casar, o motor pergunta o porte
diretamente.
"""

import unicodedata

PALAVRAS_CHAVE = {
    "baixo": [
        "catarata", "olho", "oftalmo", "dente", "dental", "odonto",
        "mama", "pele", "superficial", "hernia", "tireoide", "varizes",
        "menisco", "artroscopia", "vasectomia", "fimose", "postectomia",
    ],
    "intermediario": [
        "colecistectomia", "vesicula", "abdominal", "intraperitoneal",
        "quadril", "joelho", "protese", "artroplastia", "coluna",
        "carotida", "carotidea", "cabeca e pescoco", "histerectomia",
        "prostata", "rtu", "rim", "nefrectomia", "amigdala", "bariatrica",
    ],
    "alto": [
        "aorta", "aortico", "vascular maior", "pancreas",
        "pancreatectomia", "duodenopancreatectomia", "figado",
        "hepatectomia", "esofago", "esofagectomia", "pneumectomia",
        "pneumonectomia", "cistectomia", "adrenal", "transplante",
    ],
}


def _normalizar(texto):
    nfkd = unicodedata.normalize("NFKD", texto.lower())
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def inferir_porte(procedimento):
    """Devolve 'baixo' | 'intermediario' | 'alto' ou None se não reconhecido."""
    if not procedimento:
        return None
    texto = _normalizar(procedimento)
    # 'alto' antes de 'intermediario': procedimentos como "transplante de rim"
    # devem casar primeiro com a lista de maior risco.
    for porte in ("alto", "intermediario", "baixo"):
        for chave in PALAVRAS_CHAVE[porte]:
            if chave in texto:
                return porte
    return None
