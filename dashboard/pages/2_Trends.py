# dashboard/pages/2_Trends.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📉 Trends")

df = pd.read_csv("../data/processed/ethiopia_fi_unified_data_enriched.csv")
df['observation_date'] = pd.to_datetime(df['observation_date'])

# Filter indicators
indicators = st.multiselect(
    "Select Indicators",
    options=['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT', 'USG_DIGITAL_PAYMENT'],
    default=['ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT']
)

if indicators:
    fig, ax = plt.subplots(figsize=(10, 5))
    for ind in indicators:
        subset = df[(df['indicator_code'] == ind) & (df['gender'] == 'all')]
        if not subset.empty:
            ax.plot(subset['observation_date'], subset['value_numeric'], marker='o', label=ind)
    
    ax.set_title("Financial Inclusion Trends (2011–2024)")
    ax.set_ylabel("Percentage (%)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Data download
st.download_button(
    label="📥 Download Trend Data (CSV)",
    data=df.to_csv(index=False),
    file_name="ethiopia_fi_trends.csv",
    mime="text/csv"
)