# Tranexamic Acid (TXA) in Adult Elective Surgery and in Postpartum Haemorrhage (PPH)

**An evidence-based, knowledge-graph–ready synthesis situated within the three pillars of Patient Blood Management (PBM)**

Version 1.0 · Compiled 2026-08-10 · Companion machine-readable files: [`txa-knowledge-graph.json`](txa-knowledge-graph.json), [`txa-triples.tsv`](txa-triples.tsv)

---

## 0. Scope, method and reading conventions

### 0.1 In scope

Adult (≥18 years) **elective** surgical populations across cardiac surgery with cardiopulmonary bypass (CPB), primary total knee and hip arthroplasty (TKA/THA), spine surgery, major abdominal/hepatobiliary surgery, pelvic and gynaecologic surgery, urologic surgery, thoracic surgery, and mixed noncardiac surgery with clinically relevant bleeding risk. **PPH is treated as a distinct obstetric module** (§9), in which prophylaxis and treatment are appraised separately.

### 0.2 Out of scope (boundary conditions, cited only to delimit evidence)

Trauma (CRASH-2, CRASH-3), isolated emergency/urgent surgery (including hip fracture fixation), paediatric surgery, and non-surgical bleeding (e.g. HALT-IT in gastrointestinal bleeding). Evidence from these domains is **not** transportable to elective surgery and is flagged wherever it is mentioned.

### 0.3 Evidence labelling

Every substantive statement carries an evidence-source tag:

| Tag | Meaning |
|---|---|
| `[GUIDELINE]` | Recommendation issued by a guideline-producing body |
| `[TRIAL]` | Result of a specific randomised controlled trial (RCT) |
| `[META]` | Systematic review, meta-analysis, network meta-analysis, or individual-patient-data (IPD) meta-analysis |
| `[CONSENSUS]` | Expert consensus, pharmacologic reasoning, or practice convention without direct comparative trial evidence |

Certainty of evidence is reported as **High / Moderate / Low / Very low**. Where a guideline supplied a GRADE rating, that rating is used and attributed. Where no formal rating exists, the certainty shown is **this synthesis's own appraisal** and is explicitly marked *(appraisal)*.

### 0.4 Quality controls applied

- "Tranexamic acid (TXA)" is used consistently; **PPH = postpartum haemorrhage**.
- **Efficacy outcomes** (blood loss, transfusion, reoperation, haemoglobin, length of stay, mortality) are reported separately from **safety outcomes** (venous/arterial thromboembolism, seizure, acute kidney injury [AKI], other adverse events).
- **Absence of evidence of harm is never reported as evidence of absence of harm.** Where trials excluded high-thrombotic-risk patients, this is stated.
- Findings are **not generalised across specialties** without direct supporting evidence. Liver resection and cardiac topical administration are retained as explicit counter-examples.
- Absolute effects and 95% confidence intervals (CI) are given where available; where a figure could not be verified at source in this environment, it is marked **[unverified at source]**.

### 0.5 Verification limitation for this version

Full-text retrieval of several primary sources was blocked by network egress policy during compilation. Figures were verified through indexed search results and are attributed to the named trial/guideline. Items marked **[unverified at source]** should be confirmed against the primary publication before being used for protocol writing or regulatory submission. This is a limitation of the compilation environment, not of the underlying evidence.

---

## 1. Executive synthesis

**What TXA is.** TXA is a synthetic lysine analogue that competitively blocks the lysine-binding sites of plasminogen, preventing its binding to fibrin and thereby inhibiting fibrinolysis. It **stabilises clot that has already formed**; it does not generate thrombin, replace coagulation factors, correct anaemia, or achieve mechanical haemostasis. It is eliminated largely unchanged by the kidney, which drives both its renal dose adjustment and its dose-dependent neurotoxicity `[CONSENSUS]`.

**Where TXA sits in PBM.** TXA is a **Pillar 2** intervention — minimisation of perioperative blood loss. It does **not** substitute for Pillar 1 (detection and treatment of preoperative anaemia and iron deficiency) or Pillar 3 (restrictive, individualised transfusion practice and treatment of postoperative anaemia). The single most important interpretive error in current practice is treating universal TXA as a sufficient blood-conservation programme; WOMAN-2 is the clearest empirical demonstration that an antifibrinolytic cannot compensate for untreated anaemia `[TRIAL]` `[CONSENSUS]`.

**Established standard of care.** Three uses are supported by high or moderate certainty evidence and by guidelines:

1. **Cardiac surgery with CPB** — IV TXA reduces transfusion and reoperation for bleeding without increasing death or thrombosis; seizure risk is real and dose-dependent (ATACAS) `[TRIAL]` `[GUIDELINE]`.
2. **Primary TKA and THA** — TXA reduces blood loss and transfusion; IV, topical and oral routes are of **equivalent efficacy**, with no single route, dose or number of doses shown superior (AAHKS/AAOS/ASRA/Hip Society/Knee Society 2018, strong recommendation, high-quality evidence) `[GUIDELINE]`.
3. **Treatment of clinically diagnosed PPH** — early IV TXA (within 3 hours of birth), 1 g over 10 minutes, in addition to standard care (WHO, strong recommendation) `[GUIDELINE]` `[TRIAL]`.

**Broad but qualified support in noncardiac surgery.** POISE-3 (n = 9,535) showed TXA reduced a composite of life-threatening, major and critical-organ bleeding at 30 days (9.1% vs 11.7%; HR 0.76, 95% CI 0.67–0.87; absolute risk reduction ≈ 2.6 percentage points), while the cardiovascular safety composite was 14.2% vs 13.9% (HR 1.02, 95% CI 0.92–1.14) — a difference compatible with no harm but which **formally failed the prespecified non-inferiority margin of 1.125** `[TRIAL]`. The honest reading is: net benefit favours TXA for most patients undergoing noncardiac surgery with meaningful bleeding risk, but non-inferiority for arterial/venous thrombotic events was **not established**, and this residual uncertainty should be disclosed rather than rounded away.

**Where TXA does not work, or may harm.** Universalist framing fails at three documented points:
- **Liver resection (HeLiX, 2024):** TXA did not reduce transfusion (16.3% vs 14.5%) or blood loss (836 vs 817 mL) and perioperative complications were **significantly more common** with TXA `[TRIAL]`.
- **Topical TXA in open cardiac surgery (DEPOSITION, 2024):** topical did not reduce seizures versus IV and was **inferior for bleeding**; the trial stopped early `[TRIAL]`. Topical/IV equivalence demonstrated in arthroplasty **does not transfer** to cardiac surgery.
- **PPH prophylaxis:** prophylactic TXA is **not recommended for prevention of PPH at caesarean birth** (WHO 2025) `[GUIDELINE]`; TRAAP2 improved only a calculated-blood-loss composite without improving clinical outcomes `[TRIAL]`; the NICHD MFMU trial (n = 11,000) found no reduction in transfusion or death (3.6% vs 4.3%) `[TRIAL]`; WOMAN-2 found no reduction in clinically diagnosed PPH in anaemic women (7.0% vs 6.6%) `[TRIAL]`.

**Safety in one paragraph.** Across elective surgery, meta-analytic and trial data do not demonstrate an increase in venous thromboembolism (VTE), myocardial infarction or stroke, but the confidence intervals are wide and patients at highest thrombotic risk were frequently excluded from RCTs — this is **imprecision plus indirectness, not proof of safety** `[META]`. The one consistently demonstrated dose-dependent harm is **seizure**, concentrated in cardiac surgery with high-dose regimens (ATACAS: 0.7% vs 0.1%, p = 0.002) and amplified by renal impairment `[TRIAL]`. Renal dose reduction is mandatory in moderate-to-severe impairment `[CONSENSUS]`.

**Practical bottom line.** Give TXA when the expected blood loss is clinically relevant and the procedure sits in a specialty with direct supporting evidence; use the lowest effective dose; reduce the dose in renal impairment; do not use it to justify skipping preoperative anaemia workup; and stop assuming class-wide benefit in specialties where the trials are negative.

---

## 2. TXA within the three pillars of Patient Blood Management

PBM is a patient-centred, multidisciplinary, multimodal strategy to manage and preserve a patient's own blood. TXA occupies a defined and limited position within it.

| Pillar | Objective | Core interventions | TXA's role |
|---|---|---|---|
| **Pillar 1 — Preoperative anaemia optimisation** | Maximise endogenous red cell mass before surgery | Screening ≥4 weeks before major surgery; ferritin/TSAT/CRP; oral or IV iron; B12/folate; treat renal anaemia; erythropoiesis-stimulating agents in selected cases; defer elective surgery when feasible to allow correction | **None.** TXA has no erythropoietic effect. Using TXA as a substitute for anaemia workup is a category error `[CONSENSUS]` |
| **Pillar 2 — Minimisation of perioperative blood loss** | Reduce loss and preserve haemostasis | **TXA**; meticulous surgical technique; cell salvage; normothermia; controlled hypotension where appropriate; point-of-care viscoelastic testing; tourniquet (arthroplasty); topical haemostatic agents; structured antithrombotic bridging/interruption; minimally invasive approaches | **Primary locus of TXA.** TXA is one of several Pillar 2 measures and is additive to, not a replacement for, the others `[CONSENSUS]` `[GUIDELINE]` |
| **Pillar 3 — Management of postoperative anaemia and tolerance of anaemia** | Optimise physiological tolerance; transfuse only when indicated | Restrictive transfusion thresholds (commonly Hb 7–8 g/dL, individualised; higher in symptomatic cardiac disease); single-unit policy with reassessment; minimising diagnostic phlebotomy; postoperative iron; oxygen delivery optimisation | **None directly.** TXA reduces transfusion *exposure* by reducing loss, but does not alter the decision rule for transfusion `[CONSENSUS]` |

**Interpretation for programme design** `[CONSENSUS]`: a hospital that adopts universal TXA without an anaemia clinic, restrictive transfusion policy and cell-salvage capability has implemented approximately one-third of PBM. Contemporary PBM pathway statements (e.g. the Spanish RICA pathway) place "universal use of TXA in major surgery" **inside** Pillar 2 alongside intraoperative haemoglobin monitoring and restrictive criteria — not as a standalone programme `[GUIDELINE]`.

---

## 3. Pharmacology, routes, dosing and renal considerations

`[CONSENSUS]` unless otherwise tagged.

### 3.1 Mechanism and pharmacokinetics
- Competitive inhibition of plasminogen lysine-binding sites → reduced plasmin generation → reduced fibrin degradation.
- Predominantly renal elimination of unchanged drug (~90% within 24 h after 10 mg/kg IV). Accumulation occurs in chronic kidney disease, sustaining supratherapeutic concentrations `[META]`.
- Central nervous system effect underlying seizures: GABA-A (and glycine) receptor antagonism at high concentrations — a **concentration-dependent** phenomenon, which is why dose and renal clearance both matter.

### 3.2 Routes

| Route | Typical use | Evidence status |
|---|---|---|
| **Intravenous (IV)** | Default across all specialties | Best-evidenced route in every specialty studied `[TRIAL]` `[META]` |
| **Topical / intra-articular / local irrigation** | Arthroplasty; selected spine and other cavities | **Equivalent to IV in primary TKA/THA** `[GUIDELINE]`; **inferior to IV in open cardiac surgery (DEPOSITION)** `[TRIAL]`. Do not generalise |
| **Oral** | Arthroplasty; selected low-risk spine cases | Equivalent to IV/topical in TKA/THA `[GUIDELINE]`; requires adequate pre-incision lead time for absorption |
| **Combined (IV + topical)** | Multilevel spine, higher-bleeding-risk arthroplasty | Ranks favourably in network meta-analyses of spine surgery, low certainty *(appraisal)* `[META]` |

### 3.3 Representative dosing regimens by setting

| Setting | Regimen as studied | Source |
|---|---|---|
| Noncardiac surgery (mixed) | 1 g IV at start of surgery + 1 g IV at end | POISE-3 `[TRIAL]` |
| Cardiac surgery, low dose | 10 mg/kg bolus + 2 mg/kg/h infusion + 1 mg/kg in CPB prime | OPTIMAL `[TRIAL]` |
| Cardiac surgery, high dose | 30 mg/kg bolus + 16 mg/kg/h infusion + 2 mg/kg in CPB prime | OPTIMAL `[TRIAL]` |
| Cardiac surgery (CABG) | 100 mg/kg, protocol-amended to 50 mg/kg after seizure signal | ATACAS `[TRIAL]` |
| TKA/THA, IV | 10–20 mg/kg (commonly 1 g) pre-incision, ± second dose | AAHKS/AAOS CPG evidence base; IV doses studied ranged 10 mg/kg to 3 × 15 mg/kg `[GUIDELINE]` |
| TKA/THA, topical | 0.5–3 g intra-articular / periarticular | AAHKS/AAOS CPG evidence base `[GUIDELINE]` |
| Spine (multilevel) | Low: 10–15 mg/kg + 1–2 mg/kg/h; High: up to 100 mg/kg + 10 mg/kg/h | Network meta-analyses `[META]` |
| Liver resection | 1 g bolus after induction + 1 g over 8 h | HeLiX — **negative trial**, dose shown for completeness `[TRIAL]` |
| PPH treatment | 1 g IV over 10 min; repeat 1 g if bleeding continues after 30 min or restarts within 24 h | WHO `[GUIDELINE]` |

### 3.4 Timing
- **Elective surgery:** administer **before incision** (or before tourniquet release in arthroplasty) so that plasma concentrations are therapeutic at the moment of maximal fibrinolytic activation. In arthroplasty, pre-incision IV administration is preferred over post-incision `[GUIDELINE]`.
- **PPH:** time-critical. Benefit declines with delay; administer **within 3 hours of birth** `[GUIDELINE]` `[TRIAL]`.

### 3.5 Renal-dose considerations `[META]` `[CONSENSUS]`
- Both **body weight** and **creatinine clearance** are significant pharmacokinetic covariates; renal dysfunction prolongs supratherapeutic exposure (≈12 h above threshold in CKD stages 3–5 in modelling studies).
- Practical approach: reduce dose (and preferentially avoid high-dose or prolonged-infusion regimens) as creatinine clearance falls; published regimens stratify by serum creatinine bands (e.g. 120–249, 250–500, >500 µmol/L) with lengthened dosing intervals.
- Patients with chronic kidney disease undergoing cardiac surgery represent the **convergence of every seizure risk factor** (renal accumulation, high dose, open-chamber procedure, long bypass) and warrant the most conservative dosing.
- No universally validated renal dosing algorithm exists — this is an **evidence gap**, not a solved problem.

### 3.6 Contraindications and cautions `[CONSENSUS]` `[GUIDELINE]`
| Category | Status |
|---|---|
| Known hypersensitivity to TXA | Contraindicated |
| Active intravascular clotting / disseminated intravascular coagulation with predominant thrombosis | Contraindicated |
| Acquired defective colour vision | Contraindicated (impairs monitoring of a recognised adverse effect) |
| Subarachnoid haemorrhage | Contraindicated in most labelling (cerebral oedema/infarction concern) |
| Intrathecal / epidural administration | Absolutely contraindicated — causes seizures and death; a recognised **wrong-route medication error** with look-alike ampoules |
| Severe renal impairment | Not an absolute contraindication; **dose reduction required** |
| History of VTE, myocardial infarction, stroke, or coronary stents | The arthroplasty CPG concluded TXA is **not contraindicated** in these patients based on available evidence, but such patients were **frequently excluded from RCTs** — certainty is limited and this must not be read as demonstrated safety `[GUIDELINE]` |
| Active thromboembolic disease under treatment | Individualised risk–benefit; no adequate trial evidence |

---

## 4. Cardiac surgery with cardiopulmonary bypass

**Indication and selection** `[GUIDELINE]` `[TRIAL]`: adults undergoing elective cardiac surgery with CPB (CABG, valve, combined). Selection is essentially procedure-based rather than patient-based, because CPB reliably induces hyperfibrinolysis.

**Strategy:** IV TXA, bolus ± infusion ± pump-prime dose, started before incision and continued through bypass.

**Comparators and co-interventions:** placebo; aprotinin (historical); low- vs high-dose TXA; topical vs IV. Co-interventions: cell salvage, retrograde autologous priming, restrictive transfusion thresholds, viscoelastic-guided factor/platelet therapy, heparin/protamine management.

**Efficacy** `[TRIAL]`:
- ATACAS (n = 4,631): blood product administration 37.9% (TXA) vs 54.7% (placebo), p < 0.001; reoperation for major haemorrhage or cardiac tamponade 1.4% vs 2.8%, p = 0.001; primary composite of death and thrombotic complications at 30 days 16.7% vs 18.1% (RR 0.92, 95% CI 0.81–1.05; p = 0.22).
- OPTIMAL (n = 3,079, elective cardiac surgery with CPB): high-dose vs low-dose TXA reduced allogeneic red-cell transfusion 21.8% vs 26.0% (risk difference −4.1 percentage points, 95% CI −7.2 to −1.1).

**Safety** `[TRIAL]`:
- ATACAS: **seizure 0.7% vs 0.1%** (relative risk ≈ 7.6; p = 0.002) — the defining dose-related harm signal; the trial protocol was amended from 100 mg/kg to 50 mg/kg during conduct.
- OPTIMAL: no statistically significant difference between high and low dose in a composite of 30-day mortality, seizure, kidney dysfunction and thrombotic events; **the trial was underpowered for seizure specifically**.
- DEPOSITION (n = 3,242): topical TXA **did not reduce seizure** versus IV and produced **more bleeding events/transfusion**; stopped early; conclusion — topical should not replace IV in open cardiac surgery.

**Certainty:** High for transfusion reduction; High for the existence of a dose-dependent seizure risk; **Moderate** for the optimal dose (single-country OPTIMAL, underpowered safety) *(appraisal)*.

**Unresolved:** the dose that maximises the transfusion benefit while minimising seizures; renal-adjusted regimens; whether seizure risk translates into long-term neurocognitive harm.

---

## 5. Primary total knee and total hip arthroplasty

**Indication and selection** `[GUIDELINE]`: adults undergoing primary TKA or THA. The combined AAHKS / ASRA / AAOS / Hip Society / Knee Society clinical practice guideline (2018) supports routine use.

**Strategy** `[GUIDELINE]`:
- **Route:** IV, topical (intra-articular/periarticular) and oral are of **equivalent efficacy**. No route is superior.
- **Dose/number of doses:** no specific dose, dose regimen or number of doses has been shown superior; IV doses studied ranged from 10 mg/kg to three doses of 15 mg/kg, topical from 0.5 g to 3 g.
- **Timing:** IV TXA **before incision** is preferred to administration after incision.
- **Special populations:** the guideline concluded TXA is not contraindicated in patients with a history of VTE, myocardial infarction, cerebrovascular accident or vascular stents — with the explicit caveat that these patients were commonly excluded from the underlying RCTs.

**Comparators and co-interventions:** placebo; alternative routes/doses. Co-interventions: tourniquet use and timing of release (TKA), pneumatic compression, regional anaesthesia, restrictive transfusion, drain avoidance, chemical VTE prophylaxis (which continues unchanged — TXA does not replace or contraindicate it).

**Outcomes** `[GUIDELINE]` `[META]`: reduced calculated/total blood loss, reduced allogeneic red-cell transfusion, smaller postoperative haemoglobin decline. Transfusion in primary arthroplasty is now uncommon in TXA-treated, non-anaemic patients; length-of-stay effects are small and confounded by enhanced-recovery pathways *(appraisal)*.

**Safety** `[GUIDELINE]` `[META]`: no demonstrated increase in symptomatic VTE across pooled arthroplasty evidence; seizure is rare at arthroplasty doses. **Caveat:** power for rare thrombotic events is limited and high-risk patients were under-represented.

**Certainty:** **High** (guideline-rated) for efficacy and for route equivalence; **Moderate** for safety in patients with prior thrombotic disease.

**Unresolved:** minimal effective dose; whether oral TXA is a cost-dominant default; revision and bilateral arthroplasty regimens; interaction with modern potent VTE prophylaxis.

---

## 6. Spine surgery

**Indication and selection** `[META]`: adults undergoing instrumented, multilevel, deformity or fusion procedures where substantial blood loss is expected. Single-level microdiscectomy has little bleeding to prevent — selection should follow expected loss, not diagnosis *(appraisal)*.

**Strategy** `[META]`: IV is best evidenced. Network meta-analyses suggest higher-dose regimens (e.g. 100 mg/kg loading + 10 mg/kg/h) rank highest for blood-loss reduction, and that combined topical + IV outperforms either alone in open thoracolumbar fusion; oral TXA is proposed as a lower-intensity option in low-risk cases.

**Outcomes** `[META]`: reduced intraoperative blood loss (representative pooled mean difference ≈ −47 mL) and total estimated blood loss (≈ −210 mL); reduced transfusion (representative RR ≈ 0.68). Effect sizes vary widely between meta-analyses because of dose and procedure heterogeneity.

**Safety** `[META]`: no significant difference in thrombotic complications in pooled spine analyses; individual trials are far too small to exclude rare harm. High-dose regimens in spine surgery have **not** been evaluated for seizure with the power available in cardiac surgery — extrapolating cardiac seizure data to spine is speculative in both directions.

**Certainty:** **Moderate** for blood loss and transfusion reduction; **Low** for the superiority of any specific dose (network meta-analytic ranking with sparse direct comparisons, substantial heterogeneity) *(appraisal)*.

**Unresolved:** the dose–response ceiling; whether the high-dose ranking survives adequately powered head-to-head RCTs; seizure risk at high spine doses; deformity vs degenerative populations.

---

## 7. Major abdominal, hepatobiliary, gynaecologic, urologic and thoracic surgery

### 7.1 Mixed noncardiac surgery — the anchoring evidence

**POISE-3 (2022)** `[TRIAL]` is the largest and most directly applicable trial for elective noncardiac surgery in patients with cardiovascular risk factors.

- Population: 9,535 adults undergoing noncardiac surgery, at elevated cardiovascular risk.
- Intervention: TXA 1 g IV at start of surgery and 1 g IV at end. Comparator: placebo. Partial factorial with a hypotension-avoidance vs continuation strategy.
- **Efficacy (primary):** composite of life-threatening bleeding, major bleeding, or bleeding into a critical organ at 30 days — **9.1% vs 11.7%; HR 0.76 (95% CI 0.67–0.87), p < 0.001**; absolute risk reduction ≈ 2.6 percentage points (number needed to treat ≈ 38).
- **Safety (primary):** composite of myocardial injury after noncardiac surgery (MINS), non-haemorrhagic stroke, peripheral arterial thrombosis, symptomatic proximal VTE at 30 days — **14.2% vs 13.9%; HR 1.02 (95% CI 0.92–1.14)**. **Non-inferiority was not established** (upper CI bound exceeded the prespecified 1.125 margin; one-sided p ≈ 0.04).
- Practice implication: supports broad use in noncardiac surgery with meaningful bleeding risk, **with explicit disclosure that cardiovascular non-inferiority was not formally demonstrated**. This is a genuinely two-sided result and should not be reported as "safe" without qualification.

### 7.2 Liver resection — a negative trial that must not be overwritten

**HeLiX (JAMA, 2024)** `[TRIAL]`: adults undergoing open or minimally invasive liver resection for a cancer-related indication (n ≈ 1,384 **[unverified at source]**), TXA 1 g bolus after induction + 1 g over 8 h vs placebo.
- Red-cell transfusion within 7 days: **16.3% (TXA) vs 14.5% (placebo)** — no reduction.
- Intraoperative blood loss: **836 mL vs 817 mL** — no reduction.
- **Perioperative complications were significantly more common in the TXA group.**
- Practice implication: **do not administer routine TXA for elective liver resection** on the basis of cross-specialty extrapolation. Certainty: **Moderate to High** for absence of benefit in this population *(appraisal)*.

### 7.3 Pelvic and gynaecologic surgery (non-obstetric)

`[META]` `[CONSENSUS]` Myomectomy, hysterectomy for large fibroid uterus, and endometriosis/pelvic-clearance surgery are procedures with clinically relevant bleeding risk in which TXA is widely used. Direct RCT evidence is composed of small, heterogeneous, mostly single-centre trials showing reduced measured blood loss; transfusion effects are imprecise. POISE-3 provides indirect support where these operations were represented. **Certainty: Low to Moderate** *(appraisal)*. Co-interventions with independent effect — vasopressin/tourniquet in myomectomy, GnRH-agonist pretreatment, minimally invasive approach — are frequently co-administered and confound single-trial attribution.

### 7.4 Urologic surgery

`[META]` `[CONSENSUS]` Radical retropubic prostatectomy, open/percutaneous renal surgery and large transurethral resections have evidence from small RCTs and meta-analyses suggesting reduced blood loss and transfusion. **Specific caution:** in urinary-tract surgery with upper-tract bleeding, antifibrinolytic therapy carries a theoretical risk of **obstructive clot retention in the collecting system** — a route-specific hazard absent from other specialties. **Certainty: Low to Moderate** *(appraisal)*.

### 7.5 Thoracic surgery

`[CONSENSUS]` *(appraisal)* Elective lung resection generally involves modest transfusion rates; dedicated RCT evidence is sparse. Use is reasonable for extended resections, chest-wall resection, pleurectomy/decortication and redo thoracotomy, and is supported only **indirectly** by POISE-3. **Certainty: Very low to Low.** This is an explicit evidence gap.

### 7.6 Boundary cases explicitly excluded

Trauma (CRASH-2/CRASH-3), hip fracture and other urgent/emergency surgery, and gastrointestinal bleeding (HALT-IT, which found no mortality benefit and a signal for VTE and seizures) are **outside the elective-surgery evidence base**. They are named here solely to prevent inappropriate borrowing of effect estimates in either direction `[TRIAL]`.

---

## 8. Landmark trials

| Acronym | Full title | Year | Population | Intervention | Comparator | Primary outcome | Main finding | Practice implication |
|---|---|---|---|---|---|---|---|---|
| **POISE-3** | PeriOperative ISchemic Evaluation-3: Tranexamic Acid in Patients Undergoing Noncardiac Surgery | 2022 | 9,535 adults, noncardiac surgery, elevated CV risk | TXA 1 g IV at start + 1 g at end | Placebo | Composite life-threatening/major/critical-organ bleeding at 30 d (efficacy); MINS, non-haemorrhagic stroke, peripheral arterial thrombosis, proximal VTE (safety, non-inferiority) | Bleeding 9.1% vs 11.7%, HR 0.76 (0.67–0.87); safety 14.2% vs 13.9%, HR 1.02 (0.92–1.14), non-inferiority **not** met | Supports broad noncardiac use with disclosed residual CV uncertainty |
| **ATACAS** | Aspirin and Tranexamic Acid for Coronary Artery Surgery (TXA comparison) | 2017 | 4,631 adults, coronary artery surgery at risk of major bleeding | TXA IV (100 mg/kg, amended to 50 mg/kg) | Placebo | Composite death + thrombotic complications at 30 d | Composite 16.7% vs 18.1%, RR 0.92 (0.81–1.05), p=0.22; transfusion 37.9% vs 54.7%; reoperation for bleeding 1.4% vs 2.8%; **seizure 0.7% vs 0.1%, p=0.002** | TXA standard in cardiac surgery; use lowest effective dose |
| **OPTIMAL** | Effect of High- vs Low-Dose Tranexamic Acid Infusion on Need for Red Blood Cell Transfusion and Adverse Events in Cardiac Surgery | 2022 | 3,079 adults, elective cardiac surgery with CPB (China) | High dose (30 mg/kg + 16 mg/kg/h + 2 mg/kg prime) | Low dose (10 mg/kg + 2 mg/kg/h + 1 mg/kg prime) | Allogeneic RBC transfusion | 21.8% vs 26.0%, risk difference −4.1 pp (−7.2 to −1.1); no significant difference in composite safety events | Higher dose gives a modest transfusion gain; safety underpowered — not a mandate for high dose |
| **DEPOSITION** | Decreasing Postoperative Blood Loss by Topical vs Intravenous Tranexamic Acid in Open Cardiac Surgery | 2024 | 3,242 adults, open cardiac surgery, 16 hospitals/6 countries | Topical TXA | IV TXA | Seizure (with bleeding non-inferiority) | Topical did **not** reduce seizure; **inferior** for bleeding/transfusion; stopped early | Do not substitute topical for IV in cardiac surgery |
| **HeLiX** | Hemorrhage During Liver Resection: Tranexamic Acid | 2024 | ≈1,384 adults, liver resection for cancer indication | TXA 1 g bolus + 1 g over 8 h | Placebo | Red-cell transfusion within 7 d | 16.3% vs 14.5% (no benefit); blood loss 836 vs 817 mL; **more perioperative complications with TXA** | Do not use routine TXA for elective liver resection |
| **WOMAN** | World Maternal Antifibrinolytic Trial | 2017 | 20,060 women with clinically diagnosed PPH after vaginal or caesarean birth | TXA 1 g IV (repeat 1 g if bleeding continued/restarted) | Placebo | Composite death from all causes or hysterectomy | Composite not reduced (hysterectomy often already decided); **death due to bleeding 1.5% vs 1.9%, RR 0.81 (0.65–1.00)**; within 3 h RR 0.69 (0.52–0.91); laparotomy for bleeding RR 0.64 (0.49–0.85); no excess thromboembolism | Basis for early TXA (<3 h) as treatment of clinically diagnosed PPH |
| **WOMAN-2** | World Maternal Antifibrinolytic Trial 2 | 2024 | 15,068 women in labour with moderate/severe anaemia (Hb <100 g/L), 34 hospitals in Nigeria, Pakistan, Tanzania, Zambia | TXA 1 g IV within 15 min of cord clamping | Placebo | Clinically diagnosed PPH | **7.0% (530/7,579) vs 6.6% (497/7,478) — no reduction**; no vascular occlusive events reported in either group | Prophylactic TXA does not compensate for anaemia; **anaemia prevention (PBM Pillar 1) is the actionable lever** |
| **TRAAP** | TRAnexamic Acid for Preventing postpartum haemorrhage after vaginal delivery | 2018 | ~4,079 women, vaginal delivery | TXA 1 g IV prophylaxis + prophylactic oxytocin | Placebo + oxytocin | PPH ≥500 mL | 8.1% vs 9.8%, RR 0.83 (0.68–1.01), p = 0.07 — **not significant** | Does not support routine prophylaxis after vaginal birth |
| **TRAAP2** | TRAnexamic Acid for Preventing postpartum haemorrhage after caesarean delivery | 2021 | ~4,551 women, caesarean delivery | TXA 1 g IV prophylaxis + uterotonic | Placebo + uterotonic | Calculated blood loss >1,000 mL or red-cell transfusion by day 2 | 26.7% vs 31.6%, adjusted RR 0.84 (0.75–0.94), p = 0.003; **no difference in clinically assessed haemorrhage outcomes**; more nausea/vomiting **[secondary outcomes unverified at source]** | Calculated-composite benefit without demonstrated clinical benefit; insufficient for routine prophylaxis |
| **(NICHD MFMU)** | Tranexamic Acid to Prevent Obstetrical Hemorrhage after Cesarean Delivery (Pacheco et al.) | 2023 | 11,000 patients, caesarean delivery, 31 US MFMU hospitals | TXA 1 g IV prophylaxis | Placebo | Composite maternal death or red-cell transfusion | **3.6% vs 4.3% — not significant**; estimated blood loss >1 L 7.3% vs 8.0% | Prophylactic TXA at caesarean does not reduce transfusion or death |
| **WOMAN Trials Collaborators IPD meta-analysis** | Tranexamic acid for postpartum bleeding: systematic review and individual patient data meta-analysis | 2024 | Pooled randomised evidence, treatment and prophylaxis | TXA | Placebo/standard care | Life-threatening bleeding; death due to bleeding | TXA **substantially reduces life-threatening bleeding after childbirth**, irrespective of mode of birth or anaemia status; no increase in vascular occlusive events **[effect estimates unverified at source]** | Reconciles WOMAN-2's null PPH-incidence result with a benefit on severe-bleeding outcomes |
| **(Cochrane/Ker)** | Effect of tranexamic acid on surgical bleeding: systematic review and cumulative meta-analysis | 2012 | 129 trials, 10,488 surgical patients | TXA | Placebo/no TXA | Blood transfusion | Transfusion **RR 0.62 (95% CI 0.58–0.65)**; mortality RR 0.61 (0.38–0.98); MI RR 0.68 (0.43–1.09); stroke RR 1.14 (0.65–2.00); DVT RR 0.86 (0.53–1.39); PE RR 0.61 (0.25–1.47) **[point estimates unverified at source]** | Establishes class-level transfusion benefit; thrombotic outcomes **imprecise, not reassuring** |

---

## 9. PPH module (obstetric)

> **PPH = postpartum haemorrhage.** This module is deliberately separated from the elective-surgery evidence because obstetric physiology (peripartum hyperfibrinolysis, rapid consumptive coagulopathy), outcome definitions (calculated vs clinically diagnosed blood loss), and the guideline framework differ fundamentally.

### 9.1 Core framing statement `[GUIDELINE]` `[CONSENSUS]`

**TXA is a treatment adjunct. It is not a substitute for — and must never delay — uterotonics, resuscitation, mechanical and surgical haemorrhage control, or blood-component therapy when indicated.** The correct mental model is: TXA is given *in addition to standard care*, concurrently with, not instead of, uterine massage, oxytocin/misoprostol/carbetocin, bimanual compression, intrauterine balloon tamponade, examination for and repair of trauma, removal of retained products, compression sutures, arterial ligation/embolisation, hysterectomy when required, and structured transfusion (including fibrinogen replacement where indicated).

### 9.2 Treatment of clinically diagnosed PPH — recommended `[GUIDELINE]` `[TRIAL]`

| Element | Specification |
|---|---|
| **Indication** | Clinically diagnosed PPH following **vaginal birth or caesarean section**, regardless of cause (atony or trauma) |
| **Route** | Intravenous |
| **Dose** | **1 g (100 mg/mL) IV over 10 minutes** (rate ≈ 1 mL/min) — rapid injection risks hypotension |
| **Timing** | **As early as possible, within 3 hours of birth.** Benefit declines with delay; administration beyond 3 hours is not supported |
| **Repeat dose** | A **second 1 g IV dose** if bleeding continues after 30 minutes, or if bleeding restarts within 24 hours of the first dose |
| **Strength / certainty** | **Strong recommendation** (WHO); moderate-certainty evidence for the mortality outcome |
| **Position in care** | Part of the PPH care bundle; given **in addition to** standard care, never as a replacement |

**Evidence basis for early administration** `[TRIAL]`: in the WOMAN trial (n = 20,060), death due to bleeding was 1.5% with TXA vs 1.9% with placebo (RR 0.81, 95% CI 0.65–1.00; p = 0.045), with the effect concentrated in women treated **within 3 hours of birth** (RR 0.69, 95% CI 0.52–0.91) and no benefit demonstrated thereafter. Laparotomy to control bleeding was reduced (RR 0.64, 95% CI 0.49–0.85). The original composite primary outcome (all-cause death or hysterectomy) was not reduced, because the decision to perform hysterectomy was frequently made at or before enrolment — a design artefact, not evidence against TXA. No increase in thromboembolic events or seizures was observed. The 2024 IPD meta-analysis reinforces a reduction in life-threatening bleeding irrespective of mode of birth or anaemia status `[META]`.

**Contraindications/cautions specific to obstetrics** `[CONSENSUS]`: known hypersensitivity; acquired defective colour vision; active intravascular clotting; **never intrathecal/epidural** (fatal wrong-route error — obstetric units carrying both TXA and local anaesthetic ampoules must have physical segregation and labelling controls); dose adjustment in known renal impairment.

### 9.3 Prophylactic TXA — separate appraisal, different conclusion

**This is not the same question as treatment and must not be conflated with it.**

| Setting | Evidence | Current position |
|---|---|---|
| **Caesarean birth** | TRAAP2 `[TRIAL]`: benefit only on a **calculated** blood-loss/transfusion composite (26.7% vs 31.6%, aRR 0.84, 0.75–0.94), with no difference in clinically assessed haemorrhage outcomes. NICHD MFMU trial `[TRIAL]` (n = 11,000): composite maternal death or transfusion **3.6% vs 4.3%, not significant**; estimated blood loss >1 L 7.3% vs 8.0% | **Not recommended for prevention of PPH at caesarean birth** (WHO 2025 consolidated guidelines) `[GUIDELINE]` |
| **Vaginal birth** | TRAAP `[TRIAL]`: PPH ≥500 mL 8.1% vs 9.8%, RR 0.83 (0.68–1.01), p = 0.07 — **not significant** | **Not supported** for routine prophylaxis; uterotonic prophylaxis remains the standard `[GUIDELINE]` |
| **Women with moderate/severe anaemia** | WOMAN-2 `[TRIAL]` (n = 15,068, Hb <100 g/L): clinically diagnosed PPH **7.0% vs 6.6%** — no reduction; no vascular occlusive events reported | **Does not support** prophylaxis in anaemic women. The trial's own principal message is that **anaemia prevention and treatment**, not antifibrinolytic prophylaxis, is the intervention that matters in this population |
| **Severe-bleeding outcomes in pooled data** | 2024 IPD meta-analysis `[META]`: reduction in life-threatening bleeding regardless of birth mode or anaemia status | **Uncertain / unresolved.** Pooled severe-outcome benefit coexists with consistently null trial-level results on PPH incidence and transfusion. Whether a prophylactic strategy targeted at high-risk women is worthwhile is an **open question requiring further study** |

**Interpretive rule** `[CONSENSUS]`: an effect demonstrated on a *calculated* or composite surrogate (TRAAP2) that does not appear on clinically assessed outcomes, transfusion or death (NICHD MFMU) is **not** an adequate basis for a routine prophylaxis policy. Conversely, the pooled severe-bleeding signal is not adequate grounds to declare prophylaxis useless. The correct statement is: **prophylaxis is not recommended at caesarean birth, not supported after vaginal birth, and remains uncertain for targeted high-risk use.**

### 9.4 PPH module and PBM `[CONSENSUS]`

The obstetric case makes the PBM hierarchy visible: WOMAN-2 enrolled 15,068 anaemic women and demonstrated that a Pillar 2 drug given at the right moment does not repair a Pillar 1 deficit. Antenatal anaemia screening and iron repletion, not prophylactic antifibrinolytics, are the primary lever for reducing haemorrhage-related maternal harm in anaemic populations.

---

## 10. Structured evidence table

Abbreviations: ARR = absolute risk reduction; RR = risk ratio; HR = hazard ratio; RD = risk difference; pp = percentage points; NNT = number needed to treat; CI = 95% confidence interval.

| # | Population / procedure | Bleeding-risk category | Indication status | TXA strategy (route, dose, timing) | Comparator & key co-interventions | Efficacy outcomes (absolute, CI) | Safety outcomes | Certainty | Evidence type | Key limitation |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Elective cardiac surgery with CPB (CABG) | High | **Standard of care** | IV bolus ± infusion ± pump prime; pre-incision | Placebo; cell salvage, viscoelastic testing, restrictive thresholds | Blood products 37.9% vs 54.7% (ARR 16.8 pp); reoperation for bleeding/tamponade 1.4% vs 2.8% (ARR 1.4 pp); death+thrombosis composite RR 0.92 (0.81–1.05) | **Seizure 0.7% vs 0.1%** (p=0.002); no excess death/MI/stroke/renal failure | High (efficacy); High (seizure risk exists) | `[TRIAL]` ATACAS | Dose amended mid-trial; CABG-predominant |
| 2 | Elective cardiac surgery with CPB — dose selection | High | Conditional (dose choice) | High vs low dose IV | Low-dose TXA | RBC transfusion 21.8% vs 26.0%; RD −4.1 pp (−7.2 to −1.1) | No significant difference in 30-d mortality, seizure, renal dysfunction, thrombosis | Moderate | `[TRIAL]` OPTIMAL | Single country; underpowered for seizure |
| 3 | Open cardiac surgery — route selection | High | **Not recommended (topical)** | Topical vs IV | IV TXA | Topical **inferior** for bleeding/transfusion; trial stopped early | Topical did **not** reduce seizure | Moderate–High | `[TRIAL]` DEPOSITION | Primary outcome was seizure, not bleeding |
| 4 | Primary TKA / THA | Moderate | **Standard of care** | IV, topical or oral — equivalent; IV pre-incision preferred; IV 10 mg/kg–3×15 mg/kg, topical 0.5–3 g | Placebo; tourniquet, regional anaesthesia, restrictive transfusion, VTE prophylaxis | Reduced total/calculated blood loss; reduced allogeneic RBC transfusion; smaller Hb decline | No demonstrated increase in symptomatic VTE; seizure rare at these doses | **High** (guideline-rated) | `[GUIDELINE]` AAHKS/ASRA/AAOS/Hip/Knee 2018 | Patients with prior VTE/MI/stroke commonly excluded from source RCTs |
| 5 | TKA/THA in patients with prior VTE, MI, stroke, stents | Moderate | Conditional (not contraindicated) | As above | As above | Efficacy assumed equivalent | Guideline concluded not contraindicated; **evidence base excludes these patients** | Moderate | `[GUIDELINE]` | Indirectness; cannot infer absence of harm |
| 6 | Multilevel / instrumented spine surgery | Moderate–High | Conditional–established | IV 10–15 mg/kg + 1–2 mg/kg/h, up to 100 mg/kg + 10 mg/kg/h; combined IV+topical in open thoracolumbar fusion | Placebo; cell salvage, positioning, hypotensive anaesthesia | Intraoperative blood loss ≈ −47 mL; total estimated blood loss ≈ −210 mL; transfusion RR ≈ 0.68 | No significant difference in thrombotic complications in pooled analyses | Moderate (efficacy); **Low** (optimal dose) | `[META]` network meta-analyses | Marked heterogeneity; sparse direct comparisons; seizure not adequately studied at high dose |
| 7 | Mixed noncardiac surgery, elevated CV risk | Moderate–High | **Established, with disclosed uncertainty** | IV 1 g at start + 1 g at end | Placebo | Bleeding composite **9.1% vs 11.7%**, HR 0.76 (0.67–0.87), ARR ≈2.6 pp, NNT ≈38 | CV composite **14.2% vs 13.9%**, HR 1.02 (0.92–1.14); **non-inferiority not established** | Moderate–High (efficacy); **Moderate** (safety, inconclusive) | `[TRIAL]` POISE-3 | Non-inferiority margin not met; heterogeneous procedure mix |
| 8 | Elective liver resection (cancer indication) | High | **Not recommended** | IV 1 g bolus + 1 g over 8 h | Placebo | Transfusion 16.3% vs 14.5% (**no benefit**); blood loss 836 vs 817 mL | **Perioperative complications significantly more common with TXA** | Moderate–High (no benefit) | `[TRIAL]` HeLiX | Cancer-indication population; mechanism of harm not established |
| 9 | Pelvic/gynaecologic surgery (myomectomy, hysterectomy) | Moderate | Conditional | IV 1 g pre-incision (typical) | Placebo; vasopressin, tourniquet, GnRH pretreatment, minimally invasive approach | Reduced measured blood loss in small RCTs; transfusion effect imprecise | No specialty-specific safety signal identified; power inadequate | **Low–Moderate** *(appraisal)* | `[META]` `[CONSENSUS]` | Small single-centre trials; confounding co-interventions |
| 10 | Urologic surgery (radical prostatectomy, renal, large TURP) | Moderate | Conditional | IV 1 g pre-incision (typical) | Placebo; cell salvage, nerve-sparing technique | Reduced blood loss and transfusion in small RCTs/meta-analyses | Theoretical **clot retention/upper-tract obstruction** with antifibrinolytics in urinary-tract bleeding | **Low–Moderate** *(appraisal)* | `[META]` `[CONSENSUS]` | Small trials; route-specific hazard under-reported |
| 11 | Elective thoracic surgery (lung/chest wall resection) | Low–Moderate | **Uncertain / investigational** | No specialty-validated regimen | Placebo (few dedicated trials) | No adequately powered specialty evidence; indirect support from POISE-3 only | Not specifically characterised | **Very low–Low** *(appraisal)* | `[CONSENSUS]` | Explicit evidence gap |
| 12 | Class-level surgical evidence | Mixed | Established (transfusion) | Any TXA regimen | Placebo / no TXA | Transfusion **RR 0.62 (0.58–0.65)**; mortality RR 0.61 (0.38–0.98) | MI RR 0.68 (0.43–1.09); stroke RR 1.14 (0.65–2.00); DVT RR 0.86 (0.53–1.39); PE RR 0.61 (0.25–1.47) — **all imprecise** | Moderate (transfusion); **Low** (thrombotic safety) | `[META]` Cochrane/Ker 2012 | Older trials, small, heterogeneous; wide CIs preclude safety conclusions |
| 13 | **Clinically diagnosed PPH (treatment)** | High | **Standard of care (strong recommendation)** | IV 1 g over 10 min; **within 3 h of birth**; repeat 1 g if bleeding continues at 30 min or restarts within 24 h | Placebo + standard care; uterotonics, tamponade, compression sutures, embolisation, transfusion | Death due to bleeding **1.5% vs 1.9%**, RR 0.81 (0.65–1.00); **within 3 h RR 0.69 (0.52–0.91)**; laparotomy for bleeding RR 0.64 (0.49–0.85); composite death/hysterectomy not reduced | No increase in thromboembolic events or seizures | **Moderate–High** | `[GUIDELINE]` WHO `[TRIAL]` WOMAN | Composite primary outcome flawed by hysterectomy timing; benefit lost after 3 h |
| 14 | **Prophylaxis at caesarean birth** | Moderate | **Not recommended** | IV 1 g prophylactic | Placebo + uterotonic | TRAAP2 calculated composite 26.7% vs 31.6%, aRR 0.84 (0.75–0.94) but **no clinical-outcome benefit**; NICHD MFMU composite death/transfusion **3.6% vs 4.3%, NS**; EBL >1 L 7.3% vs 8.0% | No excess thromboembolic events; more nausea/vomiting in TRAAP2 **[unverified at source]** | **Moderate** (against routine use) | `[GUIDELINE]` WHO 2025 `[TRIAL]` | Surrogate-vs-clinical outcome divergence |
| 15 | **Prophylaxis after vaginal birth** | Low–Moderate | **Not supported** | IV 1 g prophylactic + oxytocin | Placebo + oxytocin | PPH ≥500 mL 8.1% vs 9.8%, RR 0.83 (0.68–1.01), p=0.07 | No excess thromboembolic events | Moderate (against routine use) | `[TRIAL]` TRAAP | Underpowered for severe outcomes |
| 16 | **Prophylaxis in women with moderate/severe anaemia** | High (baseline risk) | **Not supported** | IV 1 g within 15 min of cord clamping | Placebo | Clinically diagnosed PPH **7.0% vs 6.6%** — no reduction | No vascular occlusive events reported in either arm | **High** (for absence of effect on PPH incidence) | `[TRIAL]` WOMAN-2 | LMIC settings; outcome = clinically diagnosed PPH, not severe-bleeding endpoints |
| 17 | **Severe postpartum bleeding, pooled** | High | Uncertain (prophylaxis); supportive (treatment) | Any | Placebo/standard care | Reduction in life-threatening bleeding irrespective of birth mode or anaemia status **[estimates unverified at source]** | No increase in vascular occlusive events | Moderate | `[META]` IPD 2024 | Pooling of heterogeneous prophylaxis and treatment designs |

---

## 11. Certainty, applicability and unresolved questions

### 11.1 What is genuinely settled
1. TXA reduces surgical bleeding and transfusion exposure across several major elective specialties `[META]` `[TRIAL]`.
2. TXA reduces death due to bleeding when used to **treat** clinically diagnosed PPH within 3 hours `[TRIAL]` `[GUIDELINE]`.
3. Seizure risk in cardiac surgery is real and dose-dependent `[TRIAL]`.
4. Route equivalence (IV/topical/oral) holds **in primary arthroplasty** and does **not** hold in open cardiac surgery `[GUIDELINE]` `[TRIAL]`.

### 11.2 What is genuinely unsettled
| Question | Why it is unresolved |
|---|---|
| Cardiovascular safety in noncardiac surgery | POISE-3 failed its non-inferiority margin; the point estimate is neutral but the upper CI bound permits a clinically meaningful excess |
| Optimal dose in every specialty | Only cardiac surgery has a large dedicated dose-comparison trial (OPTIMAL); spine dose rankings derive from network meta-analyses with sparse direct evidence |
| Safety in patients with prior VTE, MI, stroke or stents | Systematically excluded from most RCTs; the arthroplasty guideline's "not contraindicated" reflects **absence of evidence**, not evidence of absence |
| Renal dosing | Pharmacokinetic modelling exists; no validated, prospectively tested renal dosing algorithm |
| Why TXA harmed in liver resection | Mechanism unexplained; whether it reflects the cancer population, hepatic fibrinolytic physiology, or the 8-hour infusion is unknown |
| Targeted PPH prophylaxis in high-risk women | Trial-level nulls coexist with a pooled severe-bleeding benefit |
| Thoracic, urologic and gynaecologic specialty-specific effects | Underpowered, heterogeneous, small-trial evidence base |
| Seizure risk outside cardiac surgery at high doses | Not adequately studied at spine-surgery high-dose regimens |
| Long-term outcomes | Almost all trials report ≤30-day (or ≤90-day) follow-up; functional, neurocognitive and oncologic outcomes are largely unmeasured |

### 11.3 Systematic limitations of the evidence base
- **Population exclusions:** high thrombotic risk, severe renal impairment, active malignancy with thrombosis, and pregnancy-adjacent comorbidity are recurrently excluded.
- **Outcome heterogeneity:** "blood loss" is variously measured, estimated, or calculated from haemoglobin/haematocrit; calculated composites can move when clinical outcomes do not (TRAAP2).
- **Transfusion as an outcome is threshold-dependent:** trials conducted under liberal transfusion practice inflate apparent TXA benefit relative to contemporary restrictive practice.
- **Geographic and system indirectness:** WOMAN-2 and OPTIMAL were conducted in settings whose baseline transfusion availability and thresholds differ substantially from high-income practice.
- **Publication and small-study effects** dominate the specialty-specific literature outside cardiac and arthroplasty surgery.

---

## 12. Knowledge-graph specification

### 12.1 Node types

| Type prefix | Node class | Example IDs |
|---|---|---|
| `POP:` | Population | `POP:adult_elective_surgery`, `POP:postpartum_woman_clinically_diagnosed_pph`, `POP:anaemic_woman_in_labour` |
| `PROC:` | Procedure | `PROC:cardiac_surgery_cpb`, `PROC:tka`, `PROC:tha`, `PROC:spine_fusion_multilevel`, `PROC:liver_resection`, `PROC:caesarean_delivery`, `PROC:vaginal_birth`, `PROC:noncardiac_surgery_mixed`, `PROC:myomectomy`, `PROC:radical_prostatectomy`, `PROC:thoracic_resection` |
| `RISK:` | Bleeding-risk category | `RISK:low`, `RISK:moderate`, `RISK:high` |
| `IND:` | Indication | `IND:reduce_perioperative_blood_loss`, `IND:treatment_of_pph`, `IND:prophylaxis_of_pph` |
| `INT:` | Intervention | `INT:txa` |
| `ROUTE:` | Route | `ROUTE:iv`, `ROUTE:topical`, `ROUTE:oral`, `ROUTE:combined_iv_topical` |
| `DOSE:` | Dose | `DOSE:txa_1g_iv_x2_perioperative`, `DOSE:txa_high_dose_cardiac`, `DOSE:txa_low_dose_cardiac`, `DOSE:txa_1g_iv_pph`, … |
| `TIME:` | Timing | `TIME:pre_incision`, `TIME:within_3h_of_birth`, `TIME:within_15min_cord_clamping`, `TIME:repeat_at_30min_or_restart_24h` |
| `COMP:` | Comparator | `COMP:placebo`, `COMP:iv_txa`, `COMP:low_dose_txa`, `COMP:standard_care_uterotonic` |
| `COINT:` | Co-intervention | `COINT:cell_salvage`, `COINT:tourniquet`, `COINT:restrictive_transfusion_threshold`, `COINT:uterotonics`, `COINT:uterine_tamponade`, `COINT:surgical_haemostasis`, `COINT:iv_iron`, `COINT:viscoelastic_testing` |
| `OUT:` | Efficacy outcome | `OUT:measured_blood_loss`, `OUT:calculated_blood_loss`, `OUT:allogeneic_rbc_transfusion`, `OUT:reoperation_for_bleeding`, `OUT:laparotomy_for_bleeding`, `OUT:haemoglobin_change`, `OUT:length_of_stay`, `OUT:mortality_all_cause`, `OUT:death_due_to_bleeding`, `OUT:life_threatening_bleeding`, `OUT:clinically_diagnosed_pph` |
| `SAFE:` | Safety outcome | `SAFE:venous_thromboembolism`, `SAFE:arterial_thromboembolism`, `SAFE:myocardial_infarction`, `SAFE:stroke`, `SAFE:seizure`, `SAFE:acute_kidney_injury`, `SAFE:perioperative_complications`, `SAFE:nausea_vomiting`, `SAFE:vascular_occlusive_events` |
| `EFFECT:` | Effect direction/magnitude | `EFFECT:hr_0_76_ci_0_67_0_87`, `EFFECT:arr_2_6pp`, `EFFECT:null_no_difference`, `EFFECT:increased_harm`, … |
| `CERT:` | Certainty of evidence | `CERT:high`, `CERT:moderate`, `CERT:low`, `CERT:very_low` |
| `GL:` | Guideline | `GL:who_pph_consolidated_2025`, `GL:who_txa_pph_2017`, `GL:aahks_aaos_asra_hip_knee_txa_2018`, `GL:eacts_eactaic_pbm_cardiac_2024`, `GL:cpoc_anaemia_2025` |
| `TRIAL:` | Trial / meta-analysis | `TRIAL:poise3`, `TRIAL:atacas`, `TRIAL:optimal`, `TRIAL:deposition`, `TRIAL:helix`, `TRIAL:woman`, `TRIAL:woman2`, `TRIAL:traap`, `TRIAL:traap2`, `TRIAL:nichd_mfmu_txa_cesarean`, `META:ipd_pph_2024`, `META:cochrane_ker_surgical_bleeding` |
| `CONTRA:` | Contraindication | `CONTRA:hypersensitivity`, `CONTRA:active_intravascular_clotting`, `CONTRA:acquired_defective_colour_vision`, `CONTRA:intrathecal_administration`, `CONTRA:subarachnoid_haemorrhage` |
| `GAP:` | Evidence gap | `GAP:cv_noninferiority_noncardiac`, `GAP:renal_dosing_algorithm`, `GAP:thoracic_surgery_evidence`, … |
| `PILLAR:` | PBM pillar | `PILLAR:1_preop_anaemia`, `PILLAR:2_blood_loss_minimisation`, `PILLAR:3_anaemia_tolerance_transfusion` |

### 12.2 Relation dictionary

| Relation | Domain → Range | Semantics |
|---|---|---|
| `INDICATED_FOR` | Intervention → Indication / Population / Procedure | The intervention is indicated for this purpose or group |
| `ADMINISTERED_BY` | Intervention → Route | Route of administration |
| `DOSED_AS` | Intervention/Route → Dose | Dose regimen as studied or recommended |
| `TIMED_AT` | Intervention/Dose → Timing | Timing of administration |
| `COMPARED_WITH` | Intervention/Dose/Route → Comparator | Comparator used in the cited evidence |
| `REDUCES` | Intervention → Outcome | Statistically and clinically supported reduction |
| `DOES_NOT_REDUCE` | Intervention → Outcome | Adequately studied and shown not to reduce |
| `HAS_UNCERTAIN_EFFECT_ON` | Intervention → Outcome/Safety outcome | Effect direction unresolved or imprecise |
| `ASSOCIATED_WITH` | Intervention/Dose → Safety outcome / Effect | Non-causal or safety association, including harm signals |
| `CONTRAINDICATED_IN` | Intervention → Contraindication/Population | Must not be used |
| `RECOMMENDED_BY` | Intervention/Strategy → Guideline | Guideline endorsement (or explicit non-endorsement, via a negated qualifier field) |
| `SUPPORTED_BY` | Claim/Intervention → Trial/Meta-analysis | Evidential support |
| `LIMITED_BY` | Claim/Trial → Limitation/Certainty | Constraint on interpretation |
| `REQUIRES_FURTHER_STUDY` | Intervention/Question → Evidence gap | Explicit research need |

### 12.3 Triples

The complete machine-readable set is in [`txa-knowledge-graph.json`](txa-knowledge-graph.json) (typed nodes + triples with qualifiers: `evidence_type`, `certainty`, `effect`, `source`) and [`txa-triples.tsv`](txa-triples.tsv) (flat `subject⇥predicate⇥object⇥evidence_type⇥certainty⇥source`).

Representative extract:

```
INT:txa            INDICATED_FOR             IND:reduce_perioperative_blood_loss     [GUIDELINE] high
INT:txa            ADMINISTERED_BY           ROUTE:iv                                [TRIAL] high
INT:txa            REDUCES                   OUT:allogeneic_rbc_transfusion          [META] moderate (RR 0.62, 0.58–0.65)
INT:txa            REDUCES                   OUT:death_due_to_bleeding               [TRIAL] moderate (RR 0.81, 0.65–1.00; PPH treatment)
INT:txa            DOES_NOT_REDUCE           OUT:clinically_diagnosed_pph            [TRIAL] high (WOMAN-2, prophylaxis in anaemia)
INT:txa            DOES_NOT_REDUCE           OUT:allogeneic_rbc_transfusion          [TRIAL] moderate (HeLiX, liver resection)
INT:txa            ASSOCIATED_WITH           SAFE:seizure                            [TRIAL] high (ATACAS 0.7% vs 0.1%)
INT:txa            ASSOCIATED_WITH           SAFE:perioperative_complications        [TRIAL] moderate (HeLiX)
INT:txa            HAS_UNCERTAIN_EFFECT_ON   SAFE:arterial_thromboembolism           [TRIAL] moderate (POISE-3 non-inferiority not met)
INT:txa            CONTRAINDICATED_IN        CONTRA:intrathecal_administration       [CONSENSUS] high
INT:txa            RECOMMENDED_BY            GL:who_pph_consolidated_2025            [GUIDELINE] (treatment of clinically diagnosed PPH)
INT:txa            SUPPORTED_BY              TRIAL:poise3                            [TRIAL]
INT:txa            LIMITED_BY                CERT:moderate                           (CV non-inferiority not established)
INT:txa            REQUIRES_FURTHER_STUDY    GAP:renal_dosing_algorithm              [CONSENSUS]
```

---

## 13. Sources

Verified via indexed search during compilation; full-text retrieval was blocked by network policy for several items (see §0.5).

- [Tranexamic Acid in Patients Undergoing Noncardiac Surgery (POISE-3), NEJM 2022](https://www.nejm.org/doi/full/10.1056/NEJMoa2201171) · [ACC summary](https://www.acc.org/Latest-in-Cardiology/Articles/2022/03/31/20/23/Sat-930am-POISE-3-acc-2022)
- [Tranexamic Acid in Patients Undergoing Coronary-Artery Surgery (ATACAS), NEJM 2017](https://www.nejm.org/doi/full/10.1056/NEJMoa1606424)
- [Effect of High- vs Low-Dose Tranexamic Acid Infusion … (OPTIMAL), JAMA 2022](https://jamanetwork.com/journals/jama/fullarticle/2794565)
- [Topical Versus Intravenous Tranexamic Acid in Cardiac Surgery (DEPOSITION), Circulation 2024](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.124.069606) · [ACC press release](https://www.acc.org/About-ACC/Press-Releases/2024/04/08/13/23/topical-tranexamic-acid-found-inferior-to-intravenous-administration)
- [Tranexamic Acid in Patients Undergoing Liver Resection (HeLiX), JAMA 2024](https://www.bjsacademy.com/bjs-academy/randomized-clinical-trials/tranexamic-acid-in-patients-undergoing-liver-resection-the-helix-randomized-clinical-trial) · [Sunnybrook summary](https://sunnybrook.ca/media/item.asp?c=2&i=3742&f=sunnybrook-led-trial-finds-tranexamic-acid-increases-postoperative-complications-in-liver-resection)
- [Tranexamic Acid Use in Total Joint Arthroplasty: CPG endorsed by AAHKS, ASRA, AAOS, Hip Society, Knee Society, J Arthroplasty 2018](https://pubmed.ncbi.nlm.nih.gov/30146350/) · [ASRA summary](https://asra.com/news-publications/asra-updates/blog-landing/guidelines/2019/01/01/tranexamic-acid-in-total-joint-arthroplasty-the-endorsed-clinical-practice-guides-of-aahks-asra-american-academy-of-orthopaedic-surgeons-hip-society-and-knee-society)
- [The effect of tranexamic acid on postpartum bleeding in women with moderate and severe anaemia (WOMAN-2), Lancet 2024](https://pubmed.ncbi.nlm.nih.gov/39461792/) · [Trial results page](https://woman2.lshtm.ac.uk/results/)
- [Tranexamic acid for postpartum bleeding: systematic review and IPD meta-analysis, Lancet 2024](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)02102-0/fulltext)
- [Tranexamic Acid for the Prevention of Blood Loss after Cesarean Delivery (TRAAP2), NEJM 2021](https://www.nejm.org/doi/full/10.1056/NEJMoa2028788)
- [Tranexamic Acid to Prevent Obstetrical Hemorrhage after Cesarean Delivery (NICHD MFMU), NEJM 2023](https://www.nejm.org/doi/full/10.1056/NEJMoa2207419) · [NIH news release](https://www.nih.gov/news-events/news-releases/tranexamic-acid-does-not-appear-prevent-maternal-hemorrhage-after-cesarean-delivery)
- [WHO recommendation on tranexamic acid for the treatment of postpartum haemorrhage (2017)](https://www.who.int/publications-detail-redirect/9789241550154)
- [WHO/FIGO/ICM consolidated guidelines for the prevention, diagnosis and treatment of postpartum haemorrhage (2025)](https://www.who.int/news/item/05-10-2025-global-health-agencies-issue-new-recommendations-to-help-end-deaths-from-postpartum-haemorrhage) · [Guideline summary](https://www.guidelinecentral.com/guideline/4957346/) · [Lancet Global Health commentary](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(25)00404-8/fulltext)
- [FIGO joint statement on tranexamic acid for the treatment of PPH](https://www.figo.org/joint-statement-recommendation-tranexamic-acid-treatment-pph)
- [2024 EACTS/EACTAIC Guidelines on patient blood management in adult cardiac surgery](https://academic.oup.com/ejcts/article/67/5/ezae352/7815985)
- [CPOC Guideline for the Management of Anaemia in the Perioperative Pathway (2025)](https://cpoc.org.uk/sites/cpoc/files/documents/2025-05/CPOC-AnaemiaGuideline2025.pdf)
- [Association of Anaesthetists guidelines: the use of blood components and their alternatives (2025)](https://associationofanaesthetists-publications.onlinelibrary.wiley.com/doi/10.1111/anae.16542)
- [The optimal dose of intravenous tranexamic acid for reducing blood loss in spinal surgery: a network meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11686872/) · [Comparative efficacy and safety of different tranexamic acid administration in spine surgery](https://pubmed.ncbi.nlm.nih.gov/40745411/)
- [Tranexamic Acid Dosing for Cardiac Surgical Patients With Chronic Renal Dysfunction: A New Dosing Regimen, Anesth Analg 2018](https://pubmed.ncbi.nlm.nih.gov/29309319/)
- [High-dose tranexamic acid is related to increased risk of generalized seizures after aortic valve replacement, EJCTS 2011](https://pubmed.ncbi.nlm.nih.gov/21295991/)
- [Patient blood management, anemia, and transfusion optimization across surgical specialties](https://pmc.ncbi.nlm.nih.gov/articles/PMC10066799/)

---

## 14. Intended use and disclaimer

This synthesis is a decision-support and knowledge-representation artefact for clinical teams and for downstream knowledge-graph ingestion. It does not replace clinical judgement, institutional protocol, product labelling, or the primary literature. Figures marked **[unverified at source]** must be confirmed against the primary publication before operational use.
