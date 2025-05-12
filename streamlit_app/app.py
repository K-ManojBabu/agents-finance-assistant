import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from orchestrator import orchestrator

import streamlit as st

st.title("📈 Multi-Agent Finance Assistant")

if st.button("Get Morning Brief"):
    response = orchestrator.get_market_brief()
    st.success(response)
