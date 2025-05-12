from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/scrape/earnings")
def scrape_earnings():
    url = "https://finance.yahoo.com/calendar/earnings"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    # For demo: mock earnings result
    return {"surprises": "TSMC beat by 4%, Samsung missed by 2%"}
