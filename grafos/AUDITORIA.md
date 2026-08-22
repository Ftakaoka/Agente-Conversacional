# Auditoria das arestas de evidência

Conferido em **2026-08-22** contra os resumos indexados no **PubMed**.
**18 confirmados · 4 corrigidos · 3 não constam do resumo.**

| | Estado | Significado |
|---|---|---|
| ✅ | `confirmado` | O efeito e o IC do grafo batem com o resumo. Pontua. |
| 🔁 | `corrigido` | O grafo estava **errado**; o valor foi trocado pelo do resumo. Pontua. |
| ✎ | `nao_no_resumo` | Não consta do resumo. **Exibido, mas excluído da pontuação** — só volta a valer se você conferir o texto completo. |

O motor ignora arestas ✎ ao emitir veredito. É isso que torna a auditoria mecânica em vez de decorativa:
virar um ✎ em confirmado no JSON pode mudar um veredito, e os testes vão acusar.

## O que mudou nesta passagem

Três achados que alteram o que você vai dizer no palco:

1. **FIBRES estava errado no grafo.** Eu havia afirmado razão 0,83 (0,72–0,94). O real é
   **razão 0,96, IC 95% 0,84–1,09**, margem de não-inferioridade <1,2 — não-inferior, e
   explicitamente **não superior** (P=0,50 para superioridade). O veredito não muda (F2, desfecho
   substituto) e fica mais forte: o concentrado de fibrinogênio empatou com o crioprecipitado
   num desfecho que não chega em CASA.
2. **O ferro EV saiu de `condicional` e caiu no cemitério (F3).** O co-primário do PREVENTT foi
   nulo (RR 1,03; 0,78–1,37) e o achado de readmissão que eu usava como único caminho até CASA
   **não consta do resumo**. Se você conferir no texto completo e ele existir, é só marcar
   `verificacao: "confirmado"` e o ferro volta a condicional.
3. **O WOMAN tem uma ressalva que faltava.** O desfecho **primário** era o composto morte por
   qualquer causa ou histerectomia, e ele **não foi reduzido** (RR 0,97; 0,87–1,09). O que moveu
   foi a morte por sangramento, que era componente. A aresta foi adicionada ao grafo.

Mais duas correções menores: o número de transfusão do ATACAS que eu citava (37,9% vs 54,7%)
não consta do resumo e foi trocado pelo total de unidades (4331 vs 7994); e os números de manchete
do CRASH-3 foram trocados pelos da população com pupilas reativas, que são os do resumo.

E uma atualização de fonte: a revisão Cochrane de cell salvage que eu citava era a de 2010
(RR 0,62, benefício estabelecido). A **atualização de 2023** rebaixa a certeza do agregado para
**muito baixa** (RR 0,65; 0,59–0,72), com certeza moderada apenas em subgrupos. O grafo agora
cita a versão vigente.

## Identificação dos estudos

Segundo o **PubMed**. DOIs em link, para puxar o texto completo pela biblioteca do hospital.

| Estudo | n | PMID | Citação | DOI |
|---|---|---|---|---|
| **POISE-3 (braço ácido tranexâmico)** | 9535 | [35363452](https://pubmed.ncbi.nlm.nih.gov/35363452/) | N Engl J Med 2022;386:1986-1997 | [10.1056/NEJMoa2201171](https://doi.org/10.1056/NEJMoa2201171) |
| **ATACAS** | 4631 | [27774838](https://pubmed.ncbi.nlm.nih.gov/27774838/) | N Engl J Med 2017;376:136-148 | [10.1056/NEJMoa1606424](https://doi.org/10.1056/NEJMoa1606424) |
| **FIBRES** | 735 | [31634905](https://pubmed.ncbi.nlm.nih.gov/31634905/) | JAMA 2019;322:1966-1976 | [10.1001/jama.2019.17312](https://doi.org/10.1001/jama.2019.17312) |
| **TRICS III** | 5243 | [29130845](https://pubmed.ncbi.nlm.nih.gov/29130845/) | N Engl J Med 2017;377:2133-2144 | [10.1056/NEJMoa1711818](https://doi.org/10.1056/NEJMoa1711818) |
| **FOCUS** | 2016 | [22168590](https://pubmed.ncbi.nlm.nih.gov/22168590/) | N Engl J Med 2011;365:2453-62 | [10.1056/NEJMoa1012452](https://doi.org/10.1056/NEJMoa1012452) |
| **MINT** | 3504 | [37952133](https://pubmed.ncbi.nlm.nih.gov/37952133/) | N Engl J Med 2023;389:2446-2456 | [10.1056/NEJMoa2307983](https://doi.org/10.1056/NEJMoa2307983) |
| **PREVENTT** | 487 | [32896294](https://pubmed.ncbi.nlm.nih.gov/32896294/) | Lancet 2020;396:1353-1361 | [10.1016/S0140-6736(20)31539-7](https://doi.org/10.1016/S0140-6736(20)31539-7) |
| **Revisão Cochrane — cell salvage (atualização 2023)** | 14528 | [37681564](https://pubmed.ncbi.nlm.nih.gov/37681564/) | Cochrane Database Syst Rev 2023;9:CD001888 | [10.1002/14651858.CD001888.pub5](https://doi.org/10.1002/14651858.CD001888.pub5) |
| **CRASH-2** | 20211 | [20554319](https://pubmed.ncbi.nlm.nih.gov/20554319/) | Lancet 2010;376:23-32 | [10.1016/S0140-6736(10)60835-5](https://doi.org/10.1016/S0140-6736(10)60835-5) |
| **CRASH-3** | 12737 | [31623894](https://pubmed.ncbi.nlm.nih.gov/31623894/) | Lancet 2019;394:1713-1723 | [10.1016/S0140-6736(19)32233-0](https://doi.org/10.1016/S0140-6736(19)32233-0) |
| **WOMAN** | 20060 | [28456509](https://pubmed.ncbi.nlm.nih.gov/28456509/) | Lancet 2017;389:2105-2116 | [10.1016/S0140-6736(17)30638-4](https://doi.org/10.1016/S0140-6736(17)30638-4) |
| **HALT-IT** | 12009 | [32563378](https://pubmed.ncbi.nlm.nih.gov/32563378/) | Lancet 2020;395:1927-1936 | [10.1016/S0140-6736(20)30848-5](https://doi.org/10.1016/S0140-6736(20)30848-5) |
| **PROCOAG** | 324 | [36942533](https://pubmed.ncbi.nlm.nih.gov/36942533/) | JAMA 2023;329:1367-1375 | [10.1001/jama.2023.4080](https://doi.org/10.1001/jama.2023.4080) |
| **CRYOSTAT-2** | 1604 | [37824155](https://pubmed.ncbi.nlm.nih.gov/37824155/) | JAMA 2023;330:1882-1891 | [10.1001/jama.2023.21019](https://doi.org/10.1001/jama.2023.21019) |
| **PATCH (hemorragia intracerebral)** | 190 | [27178479](https://pubmed.ncbi.nlm.nih.gov/27178479/) | Lancet 2016;387:2605-2613 | [10.1016/S0140-6736(16)30392-0](https://doi.org/10.1016/S0140-6736(16)30392-0) |
| **PROPPR** | 680 | [25647203](https://pubmed.ncbi.nlm.nih.gov/25647203/) | JAMA 2015;313:471-82 | [10.1001/jama.2015.12](https://doi.org/10.1001/jama.2015.12) |
| **Plasma profilático para INR pouco alterado (revisões sistemáticas)** | — | — | Corpo de revisões sistemáticas e estudos observacionais; sem ECR de desfecho duro que sustente a prática. | — |

## Arestas MEDIU conferidas

| | Estudo | Desfecho | Tipo | Prim. | Direção | Efeito conferido | IC 95% |
|---|---|---|---|---|---|---|---|
| 🔁 | ATACAS | Exposição a transfusão alogênica (sim/não) | `substituto` | não | `beneficio` | 4331 vs 7994 unidades de hemocomponente transfundidas na internação | — |
| 🔁 | Revisão Cochrane — cell salvage (atualização 2023) | Exposição a transfusão alogênica (sim/não) | `substituto` | sim | `beneficio` | RR 0,65 (82 ECRs, 12.520 participantes) — certeza MUITO BAIXA | 0,59–0,72 |
| 🔁 | CRASH-3 | Mortalidade em 28–30 dias | `duro` | sim | `incerto` | 12,5% vs 14,0% — RR 0,89 (pupilas reativas ao início); leve-moderado RR 0,78 | 0,80–1,00 / 0,64–0,95 |
| 🔁 | FIBRES | Unidades de hemocomponente transfundidas | `substituto` | sim | `nao_inferior` | 16,3 vs 17,0 unidades em 24 h — razão 0,96 | 0,84–1,09 |
| ✎ | Plasma profilático para INR pouco alterado (revisões sistemáticas) | Perda sanguínea estimada (mL) | `substituto` | sim | `nulo` | sem redução consistente de sangramento | — |
| ✎ | PREVENTT | Readmissão hospitalar | `duro` | não | `beneficio` | menos readmissões no grupo ferro | — |
| ✎ | PREVENTT | Hemoglobina pós-operatória | `substituto` | não | `beneficio` | Hb maior em 8 semanas e 6 meses | — |
| ✅ | ATACAS | Mortalidade em 28–30 dias | `duro` | sim | `nao_inferior` | 16,7% vs 18,1% — RR 0,92 | 0,81–1,05 |
| ✅ | ATACAS | Convulsão | `adverso` | não | `dano` | 0,7% vs 0,1% | — |
| ✅ | CRASH-2 | Mortalidade em 28–30 dias | `duro` | sim | `beneficio` | 14,5% vs 16,0% — RR 0,91 | 0,85–0,97 |
| ✅ | CRYOSTAT-2 | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | 25,3% (crio) vs 26,1% (padrão) — OR 0,96 | 0,75–1,23 |
| ✅ | FOCUS | Morte ou incapacidade funcional | `duro` | sim | `nao_inferior` | 34,7% (restritivo) vs 35,2% (liberal) — OR 1,01 | 0,84–1,22 |
| ✅ | HALT-IT | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | morte por sangramento em 5 dias 4% vs 4% (222/5956 vs 226/5981) — RR 0,99 | 0,82–1,18 |
| ✅ | HALT-IT | Evento tromboembólico | `adverso` | não | `dano` | TVP ou TEP 0,8% vs 0,4% — RR 1,85 | 1,15–2,98 |
| ✅ | MINT | Mortalidade em 28–30 dias | `duro` | sim | `incerto` | 16,9% (restritivo) vs 14,5% (liberal) — RR 1,15 | 0,99–1,34 |
| ✅ | PATCH (hemorragia intracerebral) | Morte ou incapacidade funcional | `duro` | sim | `dano` | morte ou dependência (mRS) em 3 meses — OR comum ajustada 2,05 | 1,18–3,56 |
| ✅ | POISE-3 (braço ácido tranexâmico) | Sangramento maior com significado clínico | `duro` | sim | `beneficio` | 9,1% vs 11,7% — HR 0,76 | 0,67–0,87 |
| ✅ | POISE-3 (braço ácido tranexâmico) | Composto morte / IAM / AVC / nova diálise | `duro` | sim | `incerto` | 14,2% vs 13,9% — HR 1,02 | 0,92–1,14 |
| ✅ | PREVENTT | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | 28% vs 29% — RR 1,03 | 0,78–1,37 |
| ✅ | PROCOAG | Unidades de hemocomponente transfundidas | `substituto` | sim | `nulo` | mediana 12 vs 11 U em 24 h — diferença absoluta 0,2 U | −2,99 a 3,33 |
| ✅ | PROCOAG | Evento tromboembólico | `adverso` | não | `dano` | 35% vs 24% — diferença absoluta 11 pp | 1–21 |
| ✅ | PROPPR | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | 24 h: 12,7% vs 17,0% (diferença −4,2 pp; −9,6 a 1,1; P=0,12); 30 d: 22,4% vs 26,1% (diferença −3,7 pp; −10,2 a 2,7; P=0,26) | — |
| ✅ | TRICS III | Composto morte / IAM / AVC / nova diálise | `duro` | sim | `nao_inferior` | 11,4% (restritivo) vs 12,5% — diferença absoluta −1,11 pp | −2,93 a 0,72 |
| ✅ | WOMAN | Mortalidade em 28–30 dias | `duro` | sim | `beneficio` | morte por sangramento 1,5% vs 1,9% — RR 0,81 | 0,65–1,00 |
| ✅ | WOMAN | Morte por qualquer causa ou histerectomia | `duro` | sim | `nulo` | 5,3% vs 5,5% — RR 0,97 | 0,87–1,09 |

## O que ainda falta — precisa do texto completo

Estas três arestas estão exibidas no grafo com a marca ✎ e **fora da pontuação**:

- **PREVENTT → Readmissão hospitalar** — menos readmissões no grupo ferro. NÃO VERIFICÁVEL no resumo indexado: o resumo do PREVENTT não menciona readmissões. Esta aresta está EXCLUÍDA da pontuação até ser conferida no texto completo — e era o único caminho do ferro EV até CASA.
- **PREVENTT → Hemoglobina pós-operatória** — Hb maior em 8 semanas e 6 meses. NÃO VERIFICÁVEL no resumo indexado. Substituto de qualquer modo.
- **Plasma profilático para INR pouco alterado (revisões sistemáticas) → Perda sanguínea estimada (mL)** — sem redução consistente de sangramento. Sem ensaio único indexado: afirmação apoiada em corpo de revisões, não auditável por resumo. Excluída da pontuação — o que não altera o veredito, já que é substituto.

E três coisas que resumo nenhum resolve, e que continuam sendo decisão editorial sua:

1. **Classificar o composto de sangramento do POISE-3 como desfecho `duro`.** É essa decisão que
   faz o TXA sobreviver para os pacientes P1 e P2. Defensável, mas é uma escolha, não um dado.
2. **A regra ganho × desescalada.** Aceitar não-inferioridade como vitória para a estratégia
   restritiva é um julgamento de valor sobre onde está o ganho — não sai de nenhum ensaio.
3. **As arestas `SUGERE` e `CORRIGE`.** Achado→mecanismo e intervenção→mecanismo são fisiopatologia,
   não evidência de ensaio. Nenhuma auditoria de PubMed as toca.

---

Para virar um ✎ depois de ler o artigo:

```python
import json, pathlib
p = pathlib.Path("grafos/hemostasia-pbm.json"); g = json.loads(p.read_text())
for m in g["mediu"]:
    if (m["estudo"], m["desfecho"]) == ("PREVENTT", "D_readmissao"):
        m["verificacao"] = "confirmado"
        m["auditado"] = True
        m["efeito"] = "<o valor que você leu no artigo>"
        m["ic"] = "<IC 95%>"
p.write_text(json.dumps(g, ensure_ascii=False, indent=2) + "\n")
```

Depois: `python3 -m unittest discover -s tests` e `python3 grafos/exportar_palco.py`.
