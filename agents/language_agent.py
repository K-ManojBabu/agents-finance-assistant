from fastapi import FastAPI
import openai

app = FastAPI()
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.post("/summarize")
def summarize(payload: dict):
    prompt = f"Asia tech AUM: {payload['aum']}. Earnings: {payload['summary']}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"text": response['choices'][0]['message']['content']}
