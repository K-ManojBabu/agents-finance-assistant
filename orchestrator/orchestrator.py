import requests

def get_market_brief():
    api_data = requests.get("http://localhost:8001/api/asia_tech_data").json()
    scrape_data = requests.get("http://localhost:8002/scrape/earnings").json()

    combined = {
        "aum": "22%",
        "summary": scrape_data["surprises"]
    }

    llm_response = requests.post("http://localhost:8004/summarize", json=combined).json()
    return llm_response["text"]
