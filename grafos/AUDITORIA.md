# Auditoria das arestas de evidência

Todas as arestas `MEDIU` do grafo estão marcadas com `auditado: false`.

Os efeitos e intervalos de confiança abaixo foram **curados por memória de modelo de
linguagem** e não foram conferidos contra o artigo primário. Antes de qualquer uso
público — aula, publicação, decisão clínica — cada linha precisa ser verificada e o
campo `auditado` virado para `true` no JSON.

Ordem sugerida de auditoria: primeiro os ensaios que aparecem como **sobreviventes**
(são os que você vai afirmar em voz alta), depois os do cemitério.

## Fichas de estudo

| ✓ | Estudo | n declarado | Citação a conferir |
|---|---|---|---|
| ☐ | **POISE-3 (braço ácido tranexâmico)** | 9535 | Devereaux PJ et al. Tranexamic acid in patients undergoing noncardiac surgery. N Engl J Med 2022. |
| ☐ | **ATACAS** | 4631 | Myles PS et al. Tranexamic acid in patients undergoing coronary-artery surgery. N Engl J Med 2017. |
| ☐ | **FIBRES** | 735 | Callum J et al. Effect of fibrinogen concentrate vs cryoprecipitate on blood component transfusion after cardiac surgery. JAMA 2019. |
| ☐ | **TRICS III** | 5243 | Mazer CD et al. Restrictive or liberal red-cell transfusion for cardiac surgery. N Engl J Med 2017. |
| ☐ | **FOCUS** | 2016 | Carson JL et al. Liberal or restrictive transfusion in high-risk patients after hip surgery. N Engl J Med 2011. |
| ☐ | **MINT** | 3504 | Carson JL et al. Restrictive or liberal transfusion strategy in myocardial infarction and anemia. N Engl J Med 2023. |
| ☐ | **PREVENTT** | 487 | Richards T et al. Preoperative intravenous iron to treat anaemia before major abdominal surgery. Lancet 2020. |
| ☐ | **Revisão Cochrane — cell salvage** | — | Carless PA et al. Cell salvage for minimising perioperative allogeneic blood transfusion. Cochrane Database Syst Rev. |
| ☐ | **CRASH-2** | 20211 | CRASH-2 collaborators. Effects of tranexamic acid on death, vascular occlusive events, and blood transfusion in trauma patients with significant haemorrhage. Lancet 2010. |
| ☐ | **CRASH-3** | 12737 | CRASH-3 trial collaborators. Effects of tranexamic acid on death, disability, vascular occlusive events in traumatic brain injury. Lancet 2019. |
| ☐ | **WOMAN** | 20060 | WOMAN Trial Collaborators. Effect of early tranexamic acid administration on mortality in post-partum haemorrhage. Lancet 2017. |
| ☐ | **HALT-IT** | 12009 | HALT-IT Trial Collaborators. Effects of a high-dose 24-h infusion of tranexamic acid on death and thromboembolic events in gastrointestinal bleeding. Lancet 2020. |
| ☐ | **PROCOAG** | 324 | Bouzat P et al. Effect of 4-factor prothrombin complex concentrate on blood product use in trauma patients with major bleeding. JAMA 2023. |
| ☐ | **CRYOSTAT-2** | 1604 | Davenport R et al. Early and empirical high-dose cryoprecipitate for hemorrhage after traumatic injury. JAMA 2023. |
| ☐ | **PATCH (hemorragia intracerebral)** | 190 | Baharoglu MI et al. Platelet transfusion versus standard care after acute stroke due to spontaneous cerebral haemorrhage associated with antiplatelet therapy. Lancet 2016. |
| ☐ | **PROPPR** | 680 | Holcomb JB et al. Transfusion of plasma, platelets, and red blood cells in a 1:1:1 vs a 1:1:2 ratio. JAMA 2015. |
| ☐ | **Plasma profilático para INR pouco alterado (revisões sistemáticas)** | — | Corpo de revisões sistemáticas e estudos observacionais; sem ECR de desfecho duro que sustente a prática. |

## Arestas MEDIU — efeito, IC e tipo de desfecho

| ✓ | Estudo | Desfecho | Tipo | Prim. | Direção | Efeito declarado | IC 95% |
|---|---|---|---|---|---|---|---|
| ☐ | POISE-3 (braço ácido tranexâmico) | Sangramento maior com significado clínico | `duro` | sim | `beneficio` | 9,1% vs 11,7% — HR 0,76 | 0,67–0,87 |
| ☐ | POISE-3 (braço ácido tranexâmico) | Composto morte / IAM / AVC / nova diálise | `duro` | sim | `incerto` | 14,2% vs 13,9% — HR 1,02 | 0,92–1,14 |
| ☐ | ATACAS | Mortalidade em 28–30 dias | `duro` | sim | `nao_inferior` | 16,7% vs 18,1% — RR 0,92 | 0,81–1,05 |
| ☐ | ATACAS | Exposição a transfusão alogênica (sim/não) | `substituto` | não | `beneficio` | 37,9% vs 54,7% | — |
| ☐ | ATACAS | Convulsão | `adverso` | não | `dano` | 0,7% vs 0,1% | — |
| ☐ | FIBRES | Unidades de hemocomponente transfundidas | `substituto` | sim | `nao_inferior` | razão 0,83 — não-inferior ao crioprecipitado | 0,72–0,94 |
| ☐ | TRICS III | Composto morte / IAM / AVC / nova diálise | `duro` | sim | `nao_inferior` | 11,4% (restritivo) vs 12,5% — diferença −1,11 pp | −2,93 a 0,72 |
| ☐ | FOCUS | Morte ou incapacidade funcional | `duro` | sim | `nao_inferior` | 34,7% (restritivo) vs 35,2% — OR 1,01 | 0,84–1,22 |
| ☐ | MINT | Mortalidade em 28–30 dias | `duro` | sim | `incerto` | 16,9% (restritivo) vs 14,5% (liberal) — RR 1,15 | 0,99–1,34 |
| ☐ | PREVENTT | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | co-primário morte ou transfusão até 30 dias — sem diferença | — |
| ☐ | PREVENTT | Readmissão hospitalar | `duro` | não | `beneficio` | menos readmissões no grupo ferro | — |
| ☐ | PREVENTT | Hemoglobina pós-operatória | `substituto` | não | `beneficio` | Hb maior em 8 semanas e 6 meses | — |
| ☐ | Revisão Cochrane — cell salvage | Exposição a transfusão alogênica (sim/não) | `substituto` | sim | `beneficio` | redução da exposição a sangue alogênico | — |
| ☐ | CRASH-2 | Mortalidade em 28–30 dias | `duro` | sim | `beneficio` | 14,5% vs 16,0% — RR 0,91 | 0,85–0,97 |
| ☐ | CRASH-3 | Mortalidade em 28–30 dias | `duro` | sim | `incerto` | 18,5% vs 19,8% — RR 0,94; em TCE leve-moderado RR 0,78 | 0,86–1,02 / 0,64–0,95 |
| ☐ | WOMAN | Mortalidade em 28–30 dias | `duro` | sim | `beneficio` | morte por sangramento 1,5% vs 1,9% — RR 0,81 | 0,65–1,00 |
| ☐ | HALT-IT | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | morte por sangramento em 5 dias 3,7% vs 3,8% — RR 0,99 | 0,82–1,18 |
| ☐ | HALT-IT | Evento tromboembólico | `adverso` | não | `dano` | 0,8% vs 0,4% — RR 1,85 | 1,15–2,98 |
| ☐ | PROCOAG | Unidades de hemocomponente transfundidas | `substituto` | sim | `nulo` | mediana 12 vs 11 U em 24 h — diferença 0,2 | −2,99 a 3,33 |
| ☐ | PROCOAG | Evento tromboembólico | `adverso` | não | `dano` | 35% vs 24% — diferença 11 pp | 1–21 |
| ☐ | CRYOSTAT-2 | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | 25,3% vs 26,1% — OR 0,96 | 0,75–1,23 |
| ☐ | PATCH (hemorragia intracerebral) | Morte ou incapacidade funcional | `duro` | sim | `dano` | morte ou dependência em 3 meses — OR 2,05 | 1,18–3,56 |
| ☐ | PROPPR | Mortalidade em 28–30 dias | `duro` | sim | `nulo` | 24 h: 12,7% vs 17,0% (p=0,12); 30 d: 22,4% vs 26,1% (p=0,26) | — |
| ☐ | Plasma profilático para INR pouco alterado (revisões sistemáticas) | Perda sanguínea estimada (mL) | `substituto` | sim | `nulo` | sem redução consistente de sangramento | — |

## Arestas CUSTA — eventos adversos

| ✓ | Intervenção | Desfecho adverso | Fonte | Efeito declarado |
|---|---|---|---|---|
| ☐ | Ácido tranexâmico | Convulsão | ATACAS | 0,7% vs 0,1% em cirurgia cardíaca com dose alta |
| ☐ | Ácido tranexâmico | Evento tromboembólico | HALT-IT | RR 1,85 (1,15–2,98) em hemorragia digestiva com dose alta em 24 h |
| ☐ | Concentrado de complexo protrombínico (CCP 4F) | Evento tromboembólico | PROCOAG | 35% vs 24% no uso empírico em trauma |
| ☐ | Concentrado de plaquetas | Morte ou incapacidade funcional | PATCH-ICH | OR 2,05 (1,18–3,56) na HIC sob antiagregante |
| ☐ | Fator VIIa recombinante (off-label) | Tromboembolismo arterial | meta-análises de uso off-label | aumento consistente de eventos arteriais |
| ☐ | Eritropoetina | Evento tromboembólico | corpo de evidência oncológica e perioperatória | sinal trombótico |

## Pontos que exigem atenção redobrada

Estas são as afirmações mais frágeis do grafo — se alguma estiver errada, muda o veredito:

1. **POISE-3, margem de não-inferioridade cardiovascular.** O grafo afirma que a margem
   (1,125) **não** foi atingida. Se estiver errado, o TXA perde a única ressalva séria
   que ele carrega em cirurgia eletiva não cardíaca.
2. **Tipo do desfecho de sangramento do POISE-3.** O grafo classifica o composto de
   sangramento com significado clínico como desfecho **duro**. Essa é uma decisão
   editorial defensável, não um fato — e é ela que faz o TXA sobreviver para P1 e P2.
3. **FIBRES como desfecho substituto.** O grafo joga o concentrado de fibrinogênio no
   cemitério (F2) porque o desfecho primário foi unidades transfundidas. Confirmar que
   não houve co-primário duro.
4. **PREVENTT, readmissões.** O grafo usa o achado secundário de readmissão como único
   caminho do ferro EV até CASA. Confirmar direção e magnitude.
5. **Direções `nao_inferior`.** TRICS III, FOCUS, ATACAS e FIBRES foram reclassificados
   de `nulo` para `nao_inferior`. Confirmar que cada um foi de fato desenhado como
   ensaio de não-inferioridade, com margem pré-especificada.
6. **PROCOAG, eventos tromboembólicos.** Confirmar 35% vs 24% e o intervalo da diferença.

---

Depois de auditar, virar a chave no JSON:

```python
import json, pathlib
p = pathlib.Path("grafos/hemostasia-pbm.json"); g = json.loads(p.read_text())
for m in g["mediu"]:
    if m["estudo"] == "POISE3-TXA":
        m["auditado"] = True
p.write_text(json.dumps(g, ensure_ascii=False, indent=2) + "\n")
```

O teste `test_toda_aresta_de_evidencia_esta_marcada_como_nao_auditada` vai falhar assim
que a primeira aresta for auditada — é proposital. Ajuste o teste para exigir o inverso
(que **todas** estejam auditadas) quando terminar a passagem.
