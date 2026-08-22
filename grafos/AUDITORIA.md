# Auditoria das arestas de evidência

Conferido em **2026-08-22**. Fonte: **PubMed (resumos) + texto completo do PREVENTT**.
**21 confirmadas · 4 corrigidas · 1 sem correspondência no resumo.**

| | Estado | Significado |
|---|---|---|
| ✅ | `confirmado` | Bate com a fonte. Pontua. |
| 🔁 | `corrigido` | O grafo estava **errado**; valor trocado pelo da fonte. Pontua. |
| ✎ | `nao_no_resumo` | Não consta do resumo. **Exibida, fora da pontuação.** |

O motor descarta arestas ✎ ao emitir veredito — é isso que torna a auditoria mecânica em vez de
decorativa. Virar um ✎ pode mudar um veredito, e os testes acusam. Foi exatamente o que aconteceu.

## O achado desta auditoria

**O PREVENTT mediu o próprio nó terminal do grafo — e ele não se moveu.**

Dias vivo e fora do hospital em 30 dias: **19,8 (DP 7,5) no placebo vs 19,7 (DP 7,0) no ferro EV,**
**diferença −0,1 dia (IC 95% −1,5 a 1,2)**. Não é um proxy de CASA. É CASA, medida, plana.
Tempo de internação também não diferiu (mediana 9 vs 9 dias).

Isso obrigou a criar um quinto modo de falha, **F5 — *Mediu CASA diretamente. CASA não se moveu.***
Quando um ensaio mede o nó terminal, nenhum desfecho secundário do mesmo horizonte o sobrepõe.

**E a readmissão que faltava existe.** Readmissão por complicações até 8 semanas: **51/234 (22%) vs**
**31/234 (13%), RR 0,61 (0,40–0,91)** — desfecho secundário **pré-especificado**. Readmissões totais
71 vs 38 (razão de taxas 0,54; 0,34–0,85). Até 6 meses o efeito se atenua: qualquer readmissão
RR 0,78 (0,58–1,04), não significativo.

As duas coisas são verdadeiras ao mesmo tempo porque estão em **horizontes diferentes**: a janela do
DAOH-30 fecha aos 30 dias, e o ganho de readmissão acontece entre a alta e as 8 semanas. O grafo agora
diz isso explicitamente, numa ressalva `HORIZONTE` acoplada ao veredito, em vez de engolir um dos dois.

> **A consequência incômoda:** o horizonte do nó CASA é uma **decisão editorial**, não um dado.
> Definido em 30 dias, o ferro endovenoso vai para o cemitério. Definido em 8 semanas, ele volta.
> O PREVENTT é o caso que expõe isso — e é a coisa mais honesta que este grafo tem para mostrar.

### Os outros achados do texto completo do PREVENTT

- Hb no **dia da cirurgia**: diferença média de apenas **+4,7 g/L** (2,7–6,8). Anemia corrigida em
  21% vs 10% (RR 2,06; 1,27–3,35). A mediana entre randomização e cirurgia foi de **15 dias** — curto
  demais para o efeito eritropoiético. É a explicação mais provável do resultado nulo, e não a
  ineficácia do ferro.
- Hb às **8 semanas +10,7 g/L** (7,8–13,7) e aos **6 meses +7,3 g/L** (3,6–11,1) — ou seja,
  o ferro funcionou como ferro; só não a tempo da cirurgia.
- Complicações Clavien-Dindo ≥ III: RR 0,89 (0,52–1,55). Mortalidade 30 d RR 1,01; 6 meses RR 1,19.

## O que já havia mudado na passagem pelos resumos

1. **FIBRES estava errado.** Eu afirmava razão 0,83 (0,72–0,94); o real é **0,96 (0,84–1,09)**,
   margem <1,2, P=0,50 para superioridade. Veredito segue F2 e fica mais forte.
2. **WOMAN ganhou a aresta que faltava.** O primário era o composto morte por qualquer causa ou
   histerectomia, e **não foi reduzido** (RR 0,97; 0,87–1,09).
3. **ATACAS**: o número de transfusão que eu citava não consta do resumo; trocado pelo total de
   unidades (4331 vs 7994). **CRASH-3**: números trocados pelos da população com pupilas reativas.
4. **Cochrane cell salvage**: da versão de 2010 para a **atualização de 2023**, que rebaixa a certeza
   do agregado de estabelecida para **muito baixa**.

## Identificação dos estudos

Segundo o **PubMed**. DOIs em link.

| Estudo | n | PMID | Citação | DOI |
|---|---|---|---|---|
| **POISE-3 (braço ácido tranexâmico)** | 9535 | [35363452](https://pubmed.ncbi.nlm.nih.gov/35363452/) | N Engl J Med 2022;386:1986-1997 | [10.1056/NEJMoa2201171](https://doi.org/10.1056/NEJMoa2201171) |
| **ATACAS** | 4631 | [27774838](https://pubmed.ncbi.nlm.nih.gov/27774838/) | N Engl J Med 2017;376:136-148 | [10.1056/NEJMoa1606424](https://doi.org/10.1056/NEJMoa1606424) |
| **FIBRES** | 735 | [31634905](https://pubmed.ncbi.nlm.nih.gov/31634905/) | JAMA 2019;322:1966-1976 | [10.1001/jama.2019.17312](https://doi.org/10.1001/jama.2019.17312) |
| **TRICS III** | 5243 | [29130845](https://pubmed.ncbi.nlm.nih.gov/29130845/) | N Engl J Med 2017;377:2133-2144 | [10.1056/NEJMoa1711818](https://doi.org/10.1056/NEJMoa1711818) |
| **FOCUS** | 2016 | [22168590](https://pubmed.ncbi.nlm.nih.gov/22168590/) | N Engl J Med 2011;365:2453-62 | [10.1056/NEJMoa1012452](https://doi.org/10.1056/NEJMoa1012452) |
| **MINT** | 3504 | [37952133](https://pubmed.ncbi.nlm.nih.gov/37952133/) | N Engl J Med 2023;389:2446-2456 | [10.1056/NEJMoa2307983](https://doi.org/10.1056/NEJMoa2307983) |
| **PREVENTT** 📄 | 487 | [32896294](https://pubmed.ncbi.nlm.nih.gov/32896294/) | Lancet 2020;396:1353-1361 | [10.1016/S0140-6736(20)31539-7](https://doi.org/10.1016/S0140-6736(20)31539-7) |
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

📄 = texto completo lido, não só o resumo.

## Arestas MEDIU conferidas

| | Estudo | Desfecho | Tipo | Prim. | Direção | Efeito conferido | IC 95% |
|---|---|---|---|---|---|---|---|
| 🔁 | ATACAS | Exposição a transfusão alogênica (sim/não) | `substituto` | não | `beneficio` | 4331 vs 7994 unidades de hemocomponente transfundidas na internação | — |
| 🔁 | Revisão Cochrane — cell salvage (atualização 2023) | Exposição a transfusão alogênica (sim/não) | `substituto` | sim | `beneficio` | RR 0,65 (82 ECRs, 12.520 participantes) — certeza MUITO BAIXA | 0,59–0,72 |
| 🔁 | CRASH-3 | Mortalidade em 28–30 dias | `duro` | sim | `incerto` | 12,5% vs 14,0% — RR 0,89 (pupilas reativas ao início); leve-moderado RR 0,78 | 0,80–1,00 / 0,64–0,95 |
| 🔁 | FIBRES | Unidades de hemocomponente transfundidas | `substituto` | sim | `nao_inferior` | 16,3 vs 17,0 unidades em 24 h — razão 0,96 | 0,84–1,09 |
| ✎ | Plasma profilático para INR pouco alterado (revisões sistemáticas) | Perda sanguínea estimada (mL) | `substituto` | sim | `nulo` | sem redução consistente de sangramento | — |
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
| ✅ 📄 | PREVENTT | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | morte ou transfusão até 30 dias: 28% vs 29% — RR 1,03 | 0,78–1,37 |
| ✅ 📄 | PREVENTT | Dias vivo e fora do hospital em 30 dias (DAOH-30) | `duro` | não | `nulo` | 19,8 (DP 7,5) vs 19,7 (DP 7,0) dias — diferença −0,1 | −1,5 a 1,2 |
| ✅ 📄 | PREVENTT | Readmissão hospitalar | `duro` | não | `beneficio` | readmissão por complicações até 8 semanas: 51/234 (22%) vs 31/234 (13%) — RR 0,61 | 0,40–0,91 |
| ✅ 📄 | PREVENTT | Hemoglobina pós-operatória | `substituto` | não | `beneficio` | Hb 8 semanas: diferença média +10,7 g/L; 6 meses: +7,3 g/L | 7,8–13,7 / 3,6–11,1 |
| ✅ | PROCOAG | Unidades de hemocomponente transfundidas | `substituto` | sim | `nulo` | mediana 12 vs 11 U em 24 h — diferença absoluta 0,2 U | −2,99 a 3,33 |
| ✅ | PROCOAG | Evento tromboembólico | `adverso` | não | `dano` | 35% vs 24% — diferença absoluta 11 pp | 1–21 |
| ✅ | PROPPR | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | 24 h: 12,7% vs 17,0% (diferença −4,2 pp; −9,6 a 1,1; P=0,12); 30 d: 22,4% vs 26,1% (diferença −3,7 pp; −10,2 a 2,7; P=0,26) | — |
| ✅ | TRICS III | Composto morte / IAM / AVC / nova diálise | `duro` | sim | `nao_inferior` | 11,4% (restritivo) vs 12,5% — diferença absoluta −1,11 pp | −2,93 a 0,72 |
| ✅ | WOMAN | Mortalidade em 28–30 dias | `duro` | sim | `beneficio` | morte por sangramento 1,5% vs 1,9% — RR 0,81 | 0,65–1,00 |
| ✅ | WOMAN | Morte por qualquer causa ou histerectomia | `duro` | sim | `nulo` | 5,3% vs 5,5% — RR 0,97 | 0,87–1,09 |

## O que ainda falta

- **Plasma profilático para INR pouco alterado (revisões sistemáticas) → Perda sanguínea estimada (mL)** — Sem ensaio único indexado: afirmação apoiada em corpo de revisões, não auditável por resumo. Excluída da pontuação — o que não altera o veredito, já que é substituto.

E três coisas que fonte nenhuma resolve, porque são **suas** decisões, não fatos:

1. **O horizonte do nó CASA.** Hoje 30 dias. É a decisão que manda o ferro EV para o cemitério.
2. **Classificar o composto de sangramento do POISE-3 como `duro`.** É o que faz o TXA sobreviver.
3. **A regra ganho × desescalada** e as arestas `SUGERE`/`CORRIGE`, que são fisiopatologia.

---

Para mudar o horizonte de CASA e ver o ferro voltar:

```python
# grafos/hemostasia-pbm.json → terminal.horizonte, e a regra F5 em motor_grafo/travessia.py
```
