"""Motor de triagem pré-operatória cardiovascular — Vera PreOp.AI.

Percorre os nós do protocolo consolidado (protocolos/triagem-preop-cardiovascular.json):
algoritmo híbrido ESC 2022 + ACC/AHA 2024, classificador ASA-PS e matriz de
exames NICE NG45.
"""

from .motor import Motor, Pergunta, Resultado, Sessao

__all__ = ["Motor", "Pergunta", "Resultado", "Sessao"]
