import streamlit as st
import yfinance as yf
import openai
from bs4 import BeautifulSoup
import requests

# Initialize OpenAI client (use secrets for safety in production)
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ─────────────────────────────────────
# Simulated "Agent" Functions (Simplified)
# ─────────────────────────────────────

def get_asia_tech_data(tickers="TSM,005930.KQ"):
    tickers_list = tickers.split(',')
    data = {ticker: yf.Ticker(ticker).info for ticker in tickers_list}
    return data

def scrape_earnings():
    # Replace with real scraping logic if needed
    return {"surprises": "TSMC beat estimates by 4%, Samsung missed by 2%."}

def generate_summary(aum, earnings):
    prompt = f"Asia tech exposure is {aum}. Earnings update: {earnings}"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# ─────────────────────────────────────
# Streamlit Frontend App
# ─────────────────────────────────────

st.set_page_config(page_title="Finance Assistant", page_icon="📈")
st.title("📈 Multi-Agent Finance Assistant (Streamlit Cloud)")

st.markdown("""
This assistant provides a **daily morning market brief** by analyzing Asia tech stock exposure and recent earnings.
""")

if st.button("Get Morning Market Brief"):
    try:
        with st.spinner("Fetching data and generating response..."):
            data = get_asia_tech_data()
            earnings = scrape_earnings()["surprises"]
            aum = "22%"  # Example AUM (hardcoded)

            brief = generate_summary(aum, earnings)

        st.success("✅ Market Brief Generated")
        st.markdown(f"**📢 Market Summary:**\n\n{brief}")

    except Exception as e:
        st.error("❌ An error occurred.")
        st.exception(e)
