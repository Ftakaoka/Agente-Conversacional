# Grafo de hemostasia e hemoderivados no contexto de PBM

Grafo tipado que parte de **um paciente concreto** e chega — ou não chega — a um
nó terminal único chamado **CASA** (dias vivo e fora do hospital em 30 dias).

A recuperação não é por similaridade semântica. É por **caminho**. E a explicação
é o caminho verbalizado, aresta por aresta.

## A estrutura

```
Paciente ──APRESENTA──▶ Achado ──SUGERE──▶ Mecanismo ◀──CORRIGE── Intervenção
                                                                       ▲
                                                                    TESTOU
                                                                       │
     CASA ◀──CONTA_PARA── Desfecho ◀────────MEDIU──────────────── Estudo
                             │                                      │
                             └─ substituto: sem aresta.         ELEGIVEL
                                Beco sem saída, por construção.  (computada)
```

**A regra que sustenta tudo:** só desfecho **duro** (e adverso, com sinal negativo)
tem aresta `CONTA_PARA` até CASA. Desfecho substituto — unidades transfundidas,
perda em mL, ΔHb — é beco sem saída **por construção do grafo**, não por opinião.

## Lógica de valor: ganho × desescalada

Uma intervenção que **adiciona** algo ao paciente (uma droga, um hemoderivado) só
sobrevive com **benefício** em desfecho duro primário.

Uma intervenção de **desescalada** — retirar uma exposição, como a estratégia
transfusional restritiva — sobrevive com **não-inferioridade**, porque o ganho
está fora do ensaio: recurso escasso poupado, exposição evitada, custo zero.

Sem essa distinção o grafo mandaria o achado mais sólido do PBM para o cemitério.

## As cinco lápides

| Código | Aresta que quebra | Lápide |
|---|---|---|
| **F0** | `TESTOU` | Ninguém testou. Só existe a aresta de mecanismo. |
| **F1** | `ELEGIVEL` | Foi testado — em outro paciente. |
| **F2** | `CONTA_PARA` | Mediu desfecho substituto; não há caminho até CASA. |
| **F3** | `MEDIU` | Mediu desfecho duro e deu nulo (ou pior). |
| **F4** | `CUSTA` | O custo adverso consome o ganho. |
| **F5** | `CONTA_PARA` (medida direta) | Mediu CASA diretamente. CASA não se moveu. |

O cemitério não é uma lista curada à mão. É o conjunto de caminhos que quebram,
e cada quebra tem o nome da aresta que faltou.

## Uso

```bash
python3 -m motor_grafo              # lista os pacientes
python3 -m motor_grafo P1           # navega Dona Cleusa
python3 -m motor_grafo --todos      # os três, em sequência (modo palco)
python3 -m motor_grafo --json P3    # saída estruturada
```

```python
from motor_grafo import Grafo, navegar, relatorio

grafo = Grafo()
print(relatorio(grafo, navegar(grafo, "P1")))
```

## Artefato de palco

`palco.html` é uma página autocontida (sem dependências externas além das fontes)
com o grafo clicável: escolha o paciente, escolha uma rota, veja o caminho acender
até CASA — ou o ✕ com o código da lápide no ponto exato em que rompe.

É **gerado**, não editado à mão. Depois de qualquer mudança no grafo:

```bash
python3 grafos/exportar_palco.py
```

O template fica em `palco.template.html`; o payload é a saída do próprio motor de
travessia. Se a página mostra algo, o motor produziu aquilo.

## Conteúdo

| | |
|---|---|
| Achados | 11 |
| Mecanismos | 9 |
| Intervenções | 14 (hemocomponente, hemoderivado, droga, técnica, estratégia) |
| Estudos | 17 |
| Desfechos | 12 (duro / substituto / adverso) |
| Pacientes | 3 (ortopédico, abdominal anticoagulado, cardíaco) |

## Estado da evidência

Arestas `MEDIU` conferidas em 2026-08-22 contra os resumos do PubMed, mais o texto completo do
PREVENTT: **21 confirmadas, 4 corrigidas, 1 sem correspondência no resumo.** Cada estudo
carrega `pmid` e `doi`. Ver [`AUDITORIA.md`](AUDITORIA.md).

Cada aresta declara seu estado em `verificacao`:

| | | |
|---|---|---|
| ✅ | `confirmado` | bate com o resumo — **pontua** |
| 🔁 | `corrigido` | o grafo estava errado, valor trocado pelo do resumo — **pontua** |
| ✎ | `nao_no_resumo` | não consta do resumo — **exibido, fora da pontuação** |

O motor descarta as arestas ✎ ao emitir veredito. É isso que torna a auditoria
mecânica em vez de decorativa: virar um ✎ pode mudar um veredito, e os testes
acusam. Foi o que aconteceu com o ferro EV, que saiu de condicional e caiu no
cemitério. Lido o texto completo, ele continua lá — mas por um motivo muito melhor: o
PREVENTT mediu **DAOH-30, o próprio nó CASA**, e ficou plano (−0,1 dia; −1,5 a 1,2).

## O horizonte de CASA é uma escolha

O ganho de readmissão do ferro EV é real e pré-especificado (RR 0,61; 0,40–0,91), e
acontece entre a alta e 8 semanas — **fora** da janela de 30 dias do nó terminal. Com
CASA em 30 dias, o ferro vai para o cemitério; com CASA em 8 semanas, ele volta. O grafo
diz isso numa ressalva `HORIZONTE` em vez de escolher em silêncio.

O que auditoria de resumo **não** alcança: as arestas `SUGERE` e `CORRIGE` são
fisiopatologia, não evidência de ensaio; e a classificação de um desfecho como
duro ou substituto é decisão editorial.

Isto é material didático e apoio à decisão. Não é diretriz e não substitui
julgamento clínico.
