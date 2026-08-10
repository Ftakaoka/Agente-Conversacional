# Agente Conversacional — Vera PreOp.AI

Triagem pré-operatória cardiovascular para **adultos em cirurgia eletiva não cardíaca, no momento de indicação/contemplação**.

## Componentes

| Diretório | Conteúdo |
|---|---|
| [`protocolos/`](protocolos/) | Protocolo consolidado em JSON: algoritmo híbrido ESC 2022 + ACC/AHA 2024, classificador ASA-PS, matriz de exames NICE NG45 |
| [`motor_triagem/`](motor_triagem/) | Motor Python (sem dependências) que percorre os nós N0–N11 do protocolo |
| [`tests/`](tests/) | Testes de cenário do motor (`python3 -m unittest discover -s tests`) |
| [`evidencia/txa/`](evidencia/txa/) | Síntese de evidência sobre ácido tranexâmico (TXA) em cirurgia eletiva e hemorragia pós-parto, situada nos três pilares do PBM, com grafo de conhecimento (JSON + TSV) |

## Motor de triagem

O motor é **dirigido por perguntas**: recomputa o percurso a cada chamada e, ao encontrar uma variável ausente, devolve a próxima `Pergunta`; quando nada falta, devolve o `Resultado` (ASA provisória, porte, RCRI, sinalizadores, exames recomendados/considerar/não e plano).

```python
from motor_triagem import Motor, Sessao, Resultado

motor = Motor()                      # config={"vigilancia_mins_ativa": False} para desativar MINS
sessao = Sessao()
while True:
    passo = motor.avaliar(sessao)
    if isinstance(passo, Resultado):
        break
    valor = obter_resposta(passo)    # camada conversacional (Vera) humaniza passo.texto
    sessao.responder(passo.id, valor)
```

CLI:

```bash
python3 -m motor_triagem          # modo interativo (pergunta a pergunta)
python3 -m motor_triagem --demo   # três cenários prontos: liberado, alto risco, instável
```

### Propriedades do desenho

- **Nós N0–N5 só usam anamnese** (zero exames): é onde a maioria dos pacientes resolve o caminho — o gate ESC (N3) libera <65 anos sem fatores de risco em cirurgia de porte baixo/intermediário sem nenhum exame cardiovascular.
- **Curto-circuito de segurança**: qualquer alarme de instabilidade (N1) ou ASA IV provisório (N2b) suspende o fluxo imediatamente com plano de encaminhamento.
- **Matriz NICE data-driven**: as regras porte × ASA são lidas do JSON do protocolo; condições "considerar" são resolvidas com o estado já coletado quando possível.
- **Decisões editoriais parametrizáveis**: vigilância de MINS (conflito ESC×ACC/AHA) via `config`.

### Aproximações declaradas

- RCRI: "cirurgia de alto risco" aproximada pelo porte ESC alto; "creatinina > 2" aproximada por doença renal/diálise.
- FRAIL ≥ 3 sinaliza fragilidade (avaliação geriátrica); ≥ 4 dispara o nó N10 (alternativas não cirúrgicas).
- A classe ASA-PS gerada é **provisória** — atribuição final é do anestesiologista.

## Avisos

Apoio à decisão para equipe de saúde. Não substitui julgamento clínico nem a consulta pré-anestésica.
