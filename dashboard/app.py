# dashboard/app.py
import streamlit as st

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    page_icon="🇪🇹",
    layout="wide"
)

st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")
st.markdown("""
Selam Analytics' forecasting system for Ethiopia's financial inclusion (2025–2027).  
Explore trends, event impacts, and scenario-based projections for **Access** (Account Ownership) and **Usage** (Digital Payments).
""")