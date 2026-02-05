# dashboard/pages/4_Projections.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎯 Inclusion Projections")

forecasts = pd.read_csv("../data/processed/forecasts_2025_2027.csv")

# NFIS-II Target: 70% by 2025 (but we forecast to 2027)
target = 70
base_2027 = forecasts['Access_Base'].iloc[-1]

fig, ax = plt.subplots(figsize=(8, 5))
years = [2024, 2025, 2026, 2027]
access_vals = [49, forecasts['Access_Base'].iloc[0], 
               forecasts['Access_Base'].iloc[1], base_2027]

ax.plot(years, access_vals, 'bo-', linewidth=2.5, markersize=8)
ax.axhline(y=target, color='red', linestyle='--', label='NFIS-II Target (70%)')
ax.set_title("Progress Toward NFIS-II Target (70% Account Ownership)")
ax.set_ylabel("Account Ownership (%)")
ax.set_xticks(years)
ax.legend()
ax.grid(True)

st.pyplot(fig)

if base_2027 < target:
    st.warning(f"🚨 Base forecast ({base_2027:.1f}%) falls short of 70% target by 2027.")
else:
    st.success("✅ On track to meet NFIS-II target!")

st.subheader("Answers to Consortium Questions")
st.write("""
1. **Will Ethiopia hit 70% account ownership by 2027?**  
   → Only in **optimistic scenario** (62% base case).

2. **What drives financial inclusion?**  
   → **Fayda Digital ID** for Access; **SuperApps** for Usage.

3. **Why did ownership stall post-2021?**  
   → **ID bottleneck**: Mobile money registration ≠ formal account ownership.
""")