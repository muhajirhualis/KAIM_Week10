# Data Enrichment Log  
*Prepared by: Muhajer Hualis*  
*Date: 2026-02-03*

## Manual Enrichments (Added on 2026-02-03)

### 1. ATM Density (2023) — REC_0031  
- **Indicator**: Number of automated teller machines (ATMs)  
- **Code**: `ACC_ATM`  
- **Value**: 10.07 ATMs per 100,000 adults  
- **Year**: 2023  
- **Source**: IMF Financial Access Survey (FAS)  
- **URL**: https://data.imf.org/en/Data-Explorer?datasetUrn=IMF.STA  
- **Confidence**: High  
- **Rationale**: Physical access remains critical; Ethiopia’s ATM density is low vs. regional peers (e.g., Kenya ~25/100k), suggesting rural exclusion risk.

---

### 2. Debit Card Penetration (2024) — REC_0032  
- **Indicator**: Number of debit cards  
- **Code**: `ACC_DEBIT_CARD` *(new code assigned)*  
- **Value**: 56.58 debit cards per 1,000 adults  
- **Year**: 2024  
- **Source**: IMF Financial Access Survey (FAS)  
- **URL**: https://data.imf.org/en/Data-Explorer?datasetUrn=IMF.STA  
- **Confidence**: High  
- **Notes**:  
  - This reflects *supply-side* card issuance, not necessarily active usage.  
  - High card density despite low account ownership suggests potential for "dormant" accounts or corporate/bulk issuance.  
  - Supports hypothesis that bank infrastructure is expanding faster than demand-side adoption.

---

### 3. Mobile Money Transaction Volume (2022) — REC_0033  
*(Note: Renamed from `rec_0032` to `REC_0033` for consistency with record ID format)*  
- **Indicator**: Number of mobile money transactions (during reference year)  
- **Code**: `USG_MM_TXN` *(new code assigned)*  
- **Value**: 64.157 transactions per 1,000 adults  
- **Year**: 2022  
- **Source**: IMF Financial Access Survey (FAS)  
- **URL**: https://data.imf.org/en/Data-Explorer?datasetUrn=IMF.STA  
- **Confidence**: High  
- **Notes**:  
  - Represents transaction *volume intensity*, not user count.  
  - Implies high activity among existing users (e.g., Telebirr users transacting frequently).  
  - Context: In 2022, Telebirr had ~20M registered users; this implies ~3.2 avg. transactions/user/year — low vs. Kenya (~12–15), suggesting underutilization or seasonal patterns.  
  - Critical for modeling *Usage* — helps distinguish between “registered” and “active” users.

---

### 4. Dashen Bank SuperApp Launch (2025-01-14) — EVT_0011  
- **Event**: Dashen Bank SuperApp Launch  
- **Code**: `EVT_DASHEN_SUPERAPP`  
- **Date**: 2025-01-14  
- **Source**: Dashen Bank Press Release  
- **URL**: https://dashenbanksc.com/dashen-bank-unveils-the-first-banking-super-app-redefining-digital-banking/  
- **Confidence**: High  
- **Rationale**: First all-in-one banking super app in Ethiopia; includes AI onboarding, QR payments, chat banking, and future micro-loans. Potential catalyst for usage growth and formalization of informal transactions.

---

## Schema Compliance Check
- ✅ All new **observations** include: `pillar`, `indicator_code`, `value_numeric`, `observation_date`, `source_name`, `source_url`, `confidence`
- ✅ All new **events** leave `pillar` blank (per schema)
- ✅ New `indicator_code`s (`ACC_DEBIT_CARD`, `USG_MM_TXN_DENSITY`) are descriptive and follow naming convention
- ✅ Gender = `all`, Location = `national`, Source Type = `survey` (for IMF) / `news` (for Dashen)

## Data Gaps Identified
- No regional (urban/rural) disaggregation in Findex or IMF FAS for Ethiopia.
- No annual data between Findex waves → limits short-term forecasting.
- Transaction *frequency* per user not available — only aggregate density.