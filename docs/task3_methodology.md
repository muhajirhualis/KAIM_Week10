# Task 3 Methodology: Event Impact Modeling

## Approach
- Used provided `impact_link` records as base estimates for event effects.
- Modeled impacts as **linear ramp functions**: effects begin after `lag_months`, then build linearly over an equal duration before plateauing.
- Refined magnitudes based on **historical validation** and **Ethiopia-specific context** (Sheet D: Market Nuances).

## Key Refinements
- **Telebirr → Account Ownership**: Reduced from +15pp to **+8pp** due to ID bottleneck (Fayda not yet rolled out in 2021–2024).
- **Fayda Digital ID**: Retained **+10pp** impact on Access and **−5pp** on Gender Gap, based on strong India Aadhaar analog.
- **Dashen SuperApp**: Added new link → **+3pp Access** via AI-powered onboarding (reduces KYC friction), and **+12% Usage** via “Three Click Shopping” and Chat Banking.
- **M-Pesa → Mobile Money Accounts**: Kept at **+5pp** — validated by observed doubling (4.7% → 9.45%).

## Validation Results
| Event | Predicted Δ (2021–2024) | Observed Δ | Assessment |
|------|--------------------------|------------|-----------|
| M-Pesa → ACC_MM_ACCOUNT | +5.0pp | +4.75pp | ✅ Well-calibrated |
| Telebirr → ACC_OWNERSHIP | +15.0pp | +3.0pp | ❌ Overestimated due to ID gap and Findex definition (active use ≠ registration) |
| Telebirr → USG_P2P_COUNT | +25% | >+100% | ⚠️ Underestimated network effects |

## Sources for Impact Estimates
- **Kenya (M-Pesa)**: Suri & Jack (2016), Science
- **India (Aadhaar)**: World Bank (2018), Datt & Ravallion (2020)
- **Tanzania (Interoperability)**: GSMA State of the Industry Report (2022)
- **Nigeria (SuperApp)**: FSD Africa (2024), CBN Case Study
- **Rwanda (FX Reform)**: IMF Country Report (2023)

## Key Assumptions
1. **Additive effects**: No interaction terms (e.g., Fayda + SuperApp synergy not modeled).
2. **Linear adoption**: Effects ramp linearly; no saturation or decay.
3. **National average**: Impacts apply uniformly (no urban/rural split).
4. **Event certainty**: All future events (e.g., Dashen launch) are assumed to occur as planned.

## Uncertainties
- **High**: Magnitude estimates (±30–50%) due to lack of Ethiopian pre/post data.
- **Medium**: Lag durations (real-world adoption may be faster/slower).
- **Low**: Direction of impact (all signs validated by theory and analogs).

## Limitations
- Only **5 Findex data points** (2011–2024) → prevents statistical calibration.
- No microdata → cannot model heterogeneous treatment effects.
- Future-dated "observations" excluded from validation to avoid circularity.

> This model provides a **transparent, evidence-based foundation** for forecasting in Task 4, with explicit acknowledgment of uncertainty.