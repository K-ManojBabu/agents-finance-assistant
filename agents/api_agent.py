from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/api/asia_tech_data")
def get_asia_tech_data(tickers: str = "TSM,005930.KQ"):
    tickers_list = tickers.split(',')
    data = {ticker: yf.Ticker(ticker).info for ticker in tickers_list}
    return data
