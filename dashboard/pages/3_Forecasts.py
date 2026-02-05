# dashboard/pages/3_Forecasts.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🔮 Forecasts (2025–2027)")

forecasts = pd.read_csv("../data/processed/forecasts_2025_2027.csv")

scenario = st.radio("Select Scenario", ["Pessimistic", "Base", "Optimistic"], index=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Access
ax1.fill_between(
    forecasts['Year'],
    forecasts['Access_Pessimistic'],
    forecasts['Access_Optimistic'],
    color='lightblue', alpha=0.3
)
ax1.plot(forecasts['Year'], forecasts[f'Access_{scenario}'], 'b-o', label=f'{scenario} Scenario')
ax1.set_title("Account Ownership Forecast")
ax1.set_ylabel("Access (%)")
ax1.grid(True)

# Usage
ax2.fill_between(
    forecasts['Year'],
    forecasts['Usage_Pessimistic'],
    forecasts['Usage_Optimistic'],
    color='lightgreen', alpha=0.3
)
ax2.plot(forecasts['Year'], forecasts[f'Usage_{scenario}'], 'g-s', label=f'{scenario} Scenario')
ax2.set_title("Digital Payment Usage Forecast")
ax2.set_ylabel("Usage (%)")
ax2.grid(True)

plt.tight_layout()
st.pyplot(fig)

st.subheader("Key Projected Milestones")
st.write("""
- **2025**: Fayda ID enrollment reaches 30M → +1pp Access boost.
- **2026**: Dashen SuperApp hits 5M users → +8% Usage.
- **2027**: M-Pesa interoperability fully rolled out → P2P volume doubles again.
""")