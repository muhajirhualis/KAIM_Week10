# dashboard/pages/1_Overview.py
import streamlit as st
import pandas as pd

st.title("📊 Overview")

# Load latest data
df = pd.read_csv("../data/processed/ethiopia_fi_unified_data_enriched.csv")
forecasts = pd.read_csv("../data/processed/forecasts_2025_2027.csv")

# Latest values
latest_access = df[(df['indicator_code'] == 'ACC_OWNERSHIP') & (df['gender'] == 'all')]['value_numeric'].iloc[-1]
latest_usage = df[df['indicator_code'] == 'USG_DIGITAL_PAYMENT']['value_numeric'].iloc[-1]
crossover_ratio = df[df['indicator_code'] == 'USG_CROSSOVER']['value_numeric'].iloc[-1]

col1, col2, col3 = st.columns(3)
col1.metric("Account Ownership (2024)", f"{latest_access:.0f}%")
col2.metric("Digital Payment Usage (2024)", f"{latest_usage:.0f}%")
col3.metric("P2P/ATM Crossover Ratio", f"{crossover_ratio:.2f}")

st.subheader("📈 Growth Highlights")
st.write("""
- **2021–2024**: Account ownership grew only **+3pp** despite 54M+ Telebirr users.
- **Gender Gap**: Narrowed from 20pp → 18pp (slow progress).
- **Milestone**: P2P transactions surpassed ATM withdrawals in Oct 2024.
""")

st.subheader("🔍 Key Insights")
st.write("""
1. **Mobile money ≠ financial inclusion**: Registration doesn't equal active account ownership.
2. **Fayda Digital ID is critical**: Strongest predictor of future Access growth.
3. **Usage outpaces Access**: SuperApps and interoperability drive digital payments.
""")