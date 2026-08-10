# Ácido tranexâmico (TXA) — síntese de evidência pronta para grafo de conhecimento

Síntese baseada em evidência sobre **ácido tranexâmico (TXA) em cirurgia eletiva de adultos**, com **hemorragia pós-parto (PPH)** tratada como módulo obstétrico distinto, situada nos **três pilares do Patient Blood Management (PBM)**.

> Os artefatos estão **em inglês** por exigência do vocabulário controlado do grafo (tipos de nó e relações em inglês: `INDICATED_FOR`, `REDUCES`, `DOES_NOT_REDUCE`, …). Este índice está em português para manter a consistência do repositório.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [`txa-pbm-synthesis.md`](txa-pbm-synthesis.md) | Documento principal: síntese executiva, mapeamento nos pilares do PBM, farmacologia e dose (incluindo ajuste renal), evidência por especialidade cirúrgica, tabela de ensaios de referência, tabela estruturada de evidência (17 linhas), módulo PPH (tratamento × profilaxia), certeza/limitações/lacunas, especificação do grafo, fontes |
| [`txa-knowledge-graph.json`](txa-knowledge-graph.json) | Grafo legível por máquina: **164 nós tipados** e **134 triplas** com qualificadores (`evidence_type`, `certainty`, `certainty_source`, `effect`, `context`, `polarity`, `source`, `unverified_at_source`) |
| [`txa-triples.tsv`](txa-triples.tsv) | As mesmas 134 triplas em formato plano tabulado, para ingestão direta |

## Convenções de qualidade aplicadas

- Cada afirmação é rotulada como `[GUIDELINE]`, `[TRIAL]`, `[META]` ou `[CONSENSUS]`.
- Desfechos de **eficácia** e de **segurança** são reportados separadamente.
- **Ausência de evidência de dano nunca é codificada como ausência de dano** — vira `HAS_UNCERTAIN_EFFECT_ON` + `LIMITED_BY`.
- Efeitos ficam ligados ao procedimento/população em que foram demonstrados; **não há herança entre especialidades** (contraexemplos preservados: hepatectomia no HeLiX, TXA tópico em cirurgia cardíaca no DEPOSITION).
- Efeitos absolutos e IC 95% sempre que disponíveis; números não confirmados no texto completo durante a compilação estão marcados `[unverified at source]` / `unverified_at_source: true`.

## Mensagens centrais

1. TXA é intervenção do **Pilar 2** (minimização de perda sanguínea). Não substitui o Pilar 1 (anemia/ferropenia) nem o Pilar 3 (transfusão restritiva e individualizada).
2. Padrão de cuidado estabelecido: cirurgia cardíaca com CEC, artroplastia primária de joelho/quadril, e **tratamento** de PPH clinicamente diagnosticada com TXA IV precoce (≤3 h do parto).
3. **Profilaxia de PPH não é a mesma pergunta que tratamento**: a OMS (2025) **não recomenda** TXA profilático na cesariana; TRAAP, TRAAP2, o ensaio NICHD MFMU e o WOMAN-2 não sustentam uso profilático de rotina.
4. Extrapolação entre especialidades falha: TXA **não** reduziu transfusão na hepatectomia (HeLiX) e **aumentou** complicações; TXA tópico foi **inferior** ao IV em cirurgia cardíaca (DEPOSITION).
5. O único dano dose-dependente consistentemente demonstrado é **convulsão** (ATACAS: 0,7% vs 0,1%), amplificado por disfunção renal.

## Validação

```bash
python3 -c "import json;d=json.load(open('evidencia/txa/txa-knowledge-graph.json'));print(len(d['nodes']),'nós /',len(d['triples']),'triplas')"
```

## Aviso

Artefato de apoio à decisão e de representação de conhecimento. Não substitui julgamento clínico, protocolo institucional, bula ou a literatura primária.
