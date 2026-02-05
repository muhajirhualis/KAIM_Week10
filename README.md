# **Interim Report: Financial Inclusion Forecasting in Ethiopia**  
**Prepared By: Muhajer Hualis**  
*Interim Submission – 1 February 2026*

---

## **1. Understanding the Business Objective**

Ethiopia is undergoing a historic digital financial transformation. With over **54 million Telebirr users**, the entry of **M-Pesa (10.8M users)**, and the landmark milestone where **P2P digital transfers surpassed ATM cash withdrawals**, the country stands at an inflection point.

Yet, the **2024 Global Findex survey reveals a paradox**: only **49% of Ethiopian adults have a financial account**—a mere **+3 percentage points** since 2021. This stagnation, despite massive mobile money adoption, raises critical questions for policymakers and industry stakeholders.

### **Consortium Goals**
Selam Analytics has been engaged by a consortium comprising:
- **Development Finance Institutions** (tracking progress toward SDG 8.10),
- **Mobile Money Operators** (Telebirr, M-Pesa) seeking market intelligence,
- **National Bank of Ethiopia** (monitoring NFIS-II targets).

Their shared objective: **forecast Ethiopia’s financial inclusion trajectory for 2025–2027** across two core dimensions defined by the **World Bank’s Global Findex**:
1. **Access**: *Account Ownership Rate* (% of adults with a bank or mobile money account).
2. **Usage**: *Digital Payment Adoption Rate* (% using digital payments in the past year).

Timely, evidence-based forecasts are essential to:
- Guide policy interventions (e.g., digital ID rollout, agent network expansion),
- Inform private-sector investment (e.g., SuperApp features, credit products),
- Track progress toward Ethiopia’s **NFIS-II target of 70% account ownership by 2025**.

---

## **2. Discussion of Completed Work and Initial Analysis**

### **Task 1: Data Exploration and Enrichment**

We adopted the provided **unified schema**, which structures all records—observations, events, impact links, and targets—into a single table. Key design principles were respected:
- **Events** (e.g., product launches, policies) carry no `pillar` assignment.
- **Impact links** explicitly connect events to indicators via `parent_id`, capturing direction, magnitude, lag, and evidence basis.

#### **Data Enrichment**
We added **5 high-value records** with full documentation in `data_enrichment_log.md`:

| Record | Type | Description | Source |
|--------|------|-------------|--------|
| `REC_0031` | Observation | ATM density (10.07/100k adults, 2023) | IMF FAS |
| `REC_0032` | Observation | Debit cards (56.58/1,000 adults, 2024) | IMF FAS |
| `REC_0033` | Observation | Mobile money transactions (64.16/1,000 adults, 2022) | IMF FAS |
| `EVT_0011` | Event | Dashen Bank SuperApp Launch (Jan 2025) | Dashen Press Release |
| Gender-disaggregated ownership (2021) | Observation | Male: 56%, Female: 36% | Findex |

All additions include `source_url`, `confidence` (“high” for IMF/Findex), and rationale.

#### **Data Quality Assessment**
- **Confidence**: 31/34 observations rated “high” confidence (Findex, IMF, official reports).
- **Temporal Coverage**: Sparse—only **5 data points for Access (2011–2024)** due to Findex’s triennial cycle.
- **Gaps**: No urban/rural splits; future-dated “observations” (2025+) treated as projections.

---

### **Task 2: Exploratory Data Analysis – 5 Key Insights**

#### **Insight 1: Account Ownership Growth Has Stalled Despite Mobile Money Expansion**  
![Account Ownership Trajectory](../reports/figures/access_trajectory.png)  
- **2017–2021**: +11pp growth (**+2.75pp/year**).  
- **2021–2024**: +3pp growth (**+1.0pp/year**).  
- **Conclusion**: Mobile money registration **does not equate to Findex-defined account ownership**. Most Ethiopians require a **bank account** for wages/savings; mobile money is complementary.

#### **Insight 2: A Persistent Gender Gap Undermines Inclusion**  
![Gender Gap](../reports/figures/gender_gap_access.png)  
- **2021**: 56% male vs. 36% female ownership (**20pp gap**).  
- **2024**: Gap narrowed slightly to **18pp**, but female mobile money usage remains critically low (**14%**).  
- **Driver**: Lack of formal ID disproportionately affects women—a barrier **Fayda Digital ID** aims to solve.

#### **Insight 3: Digital Payments Are Driven by Banks, Not Mobile Money Alone**  
![Digital Payment vs. MM](../reports/figures/digital_payment_vs_mm.png)  
- **Mobile money accounts**: **9.45%** (2024).  
- **Any digital payment usage**: **~35%** (2024).  
- **Implication**: **Bank-led innovation** (Dashen SuperApp, QR payments) and **interoperability** (EthSwitch) are primary usage drivers.

#### **Insight 4: Massive Dormancy in Mobile Money Registrations**  
![Registered vs. Active](../reports/figures/registered_vs_active_gap.png)  
- **Telebirr registered**: **64.5%** of adults (54.8M users).  
- **Findex-reported active users**: **9.45%**.  
- **Gap**: **55.1pp**—highlighting Ethiopia’s **“registration ≠ inclusion”** reality.

#### **Insight 5: Events Show Enabling, Not Direct, Impacts**  
![Event Timeline](../reports/figures/event_timeline.png)  
- **Telebirr (May 2021)**: No acceleration in account ownership post-launch.  
- **M-Pesa (Aug 2023)**: Likely contributed to mobile money doubling (4.7% → 9.45%), but causality unproven.  
- **Safaricom (Aug 2022)**: Drove infrastructure (4G) and affordability, not direct inclusion.  

> **Preliminary Impact Insight**: Mobile money’s real impact is on **transaction volume** (P2P), not account ownership. **Fayda ID** is the strongest predictor of future Access growth.

---

## **3. Next Steps and Key Areas of Focus**

### **Task 3: Event Impact Modeling**
- Build an **event-indicator association matrix** using impact links (e.g., Fayda ID → +10pp Access over 24 months).  
- **Test hypotheses**:  
  - H1: Fayda enrollment drives Access growth (India Aadhaar analog).  
  - H2: Smartphone penetration predicts Usage better than mobile money accounts.  
- Validate against historical data (e.g., Telebirr’s effect on P2P volume).

### **Task 4: Forecasting (2025–2027)**
- **Approach**: Trend regression + event-augmented scenarios (optimistic/base/pessimistic).  
- **Key Uncertainties**:  
  - Fayda ID adoption rate,  
  - SuperApp user uptake,  
  - Policy stability (FX reforms).  
- **Output**: Forecasts with **wide confidence intervals** reflecting data sparsity.

### **Task 5: Dashboard Development**
- **Streamlit app** with 4+ interactive views:  
  1. **Overview**: Key metrics (Access, Usage, P2P/ATM ratio).  
  2. **Trends**: Time-series with event overlays.  
  3. **Forecasts**: Scenario selector (2025–2027).  
  4. **Inclusion Projections**: Progress toward 70% target.  

### **Critical Data Limitations to Address**
- **No annual Findex data** → reliance on proxy indicators (IMF FAS, operator reports).  
- **Future-dated "observations"** → must be excluded from historical analysis.  
- **Urban/rural gaps** → limits granular targeting.

---

## **4. Conclusion**

Ethiopia’s financial inclusion story is defined by a **supply-demand mismatch**: infrastructure (4G, smartphones, agents) is scaling rapidly, but **demand-side barriers** (ID gaps, gender norms, trust) constrain formal account ownership. Our analysis confirms that **mobile money alone cannot drive Findex-defined inclusion**—structural enablers like **Fayda Digital ID** and **bank-led innovation** (SuperApps) are pivotal.

The next phase will quantify these relationships through **impact modeling** and deliver actionable **forecasts for 2025–2027**, empowering the consortium to make evidence-based decisions in this transformative era.

---  
**Prepared by**: Muhajer Hualis  
**Date**: 3 February 2026
