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

**Todas as arestas `MEDIU` estão com `auditado: false`.** Os efeitos e intervalos
de confiança foram curados por memória de modelo de linguagem e **não** foram
conferidos contra o artigo primário. Ver [`AUDITORIA.md`](AUDITORIA.md) — 47 itens
para conferir, com os seis pontos frágeis listados no fim.

Isto é material didático e apoio à decisão. Não é diretriz e não substitui
julgamento clínico.
