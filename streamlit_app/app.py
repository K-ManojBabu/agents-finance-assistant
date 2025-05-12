import streamlit as st
from orchestrator import orchestrator

st.title("📈 Multi-Agent Finance Assistant")

if st.button("Get Morning Brief"):
    response = orchestrator.get_market_brief()
    st.success(response)
