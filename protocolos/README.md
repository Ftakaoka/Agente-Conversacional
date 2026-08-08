# Protocolos de triagem — Vera PreOp.AI

> Motor executável destes protocolos: pacote [`motor_triagem/`](../motor_triagem/) (ver README na raiz).

## `triagem-preop-cardiovascular.json`

Protocolo consolidado de triagem pré-operatória cardiovascular para **pacientes adultos em cirurgia eletiva não cardíaca, no momento de indicação/contemplação** (antes do agendamento).

### Composição

O arquivo encadeia quatro módulos derivados de quatro fontes:

| Módulo | Fonte | Função |
|---|---|---|
| `algoritmo_hibrido` | ESC 2022 (espinha) + ACC/AHA 2024 (enxertos) | Fluxo de decisão em 12 nós (N0–N11) |
| `classificador_asa_ps` | ASA Physical Status Classification System | Classe ASA provisória por anamnese (chamado em N2b) |
| `porte_cirurgico` | ESC 2022 + mapeamento NICE | Risco do procedimento por lookup (chamado em N2) |
| `matriz_exames_nice` | NICE NG45 | Exames recomendados/não recomendados por porte × ASA (chamada em N6) |

### Encadeamento

```
N0 contexto → N1 instabilidade? → N2 porte (ESC) → N2b ASA-PS provisória
→ N3 gate do paciente (ESC: ≥65 ou fatores de risco)
→ N4 fragilidade (ACC/AHA, ≥65) → N5 capacidade funcional (DASI/proxy METs)
→ N6 exames de entrada (ESC + matriz NICE) → N7 escore RCRI (ACC/AHA)
→ N8 "o teste muda a conduta?" (ACC/AHA) → N9 imagem de estresse (ESC⊂N8)
→ N10 alternativas não cirúrgicas (ACC/AHA) → N11 decisão compartilhada e plano
```

Propriedade central do desenho: **os nós N0–N5 são cobertos integralmente por anamnese** (zero exames, zero custo) — é onde a maioria dos pacientes resolve seu caminho. Exames só aparecem de N6 em diante, sempre condicionados ao freio N8.

### Decisões editoriais (conflitos entre diretrizes)

Registradas em `conflitos_resolvidos` no próprio JSON:

1. **Vigilância de troponina (MINS)** — adotada a posição ESC (Classe I) como item de planejamento; parametrizável via `vigilancia_mins_ativa`.
2. **Imagem de estresse** — indicação ESC subordinada ao nó ACC/AHA "muda a conduta?" (N8).
3. **Gate etário** — mantido o critério ESC (≥65 anos ou fatores de risco), por ser operacionalizável com anamnese pura; escore RCRI entra depois como refinamento.

### Avisos

- A classe ASA-PS da triagem é **provisória**; a atribuição final é do anestesiologista.
- O protocolo é apoio à decisão — não substitui julgamento clínico nem a consulta pré-anestésica.
- Sinalizador de instabilidade (N1/ASA IV) **suspende** o fluxo eletivo e exige encaminhamento imediato.

### Fontes

- ESC 2022 — Guidelines on cardiovascular assessment and management of patients undergoing non-cardiac surgery
- AHA/ACC 2024 — Guideline for Perioperative Cardiovascular Management for Noncardiac Surgery
- ASA Physical Status Classification System (versão vigente, com exemplos aprovados)
- NICE NG45 — Routine preoperative tests for elective surgery
