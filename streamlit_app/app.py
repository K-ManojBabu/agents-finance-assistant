import streamlit as st
import yfinance as yf
import openai
from bs4 import BeautifulSoup
import requests

# Optional: You can replace this with st.secrets["OPENAI_API_KEY"]
openai.api_key = "your-openai-api-key"  # Replace with your key or use st.secrets

# ───────────────────────────────
# Simulated Agent Functions
# ───────────────────────────────

def get_asia_tech_data(tickers="TSM,005930.KQ"):
    tickers_list = tickers.split(',')
    data = {ticker: yf.Ticker(ticker).info for ticker in tickers_list}
    return data

def scrape_earnings():
    # Simple mock for now; scraping real data from Yahoo requires heavy parsing
    return {"surprises": "TSMC beat estimates by 4%, Samsung missed by 2%."}

def generate_summary(aum, earnings):
    prompt = f"Asia tech exposure is {aum}. Earnings update: {earnings}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# ───────────────────────────────
# Streamlit App
# ───────────────────────────────

st.title("📈 Multi-Agent Finance Assistant (Simplified)")

if st.button("Get Morning Market Brief"):
    try:
        with st.spinner("Fetching data..."):
            data = get_asia_tech_data()
            earnings = scrape_earnings()["surprises"]
            aum = "22%"  # Static for demo. Replace with logic if needed.

            brief = generate_summary(aum, earnings)

        st.success("✅ Market Brief Generated")
        st.markdown(f"**Response:** {brief}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
