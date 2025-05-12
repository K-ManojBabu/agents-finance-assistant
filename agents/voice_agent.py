from fastapi import FastAPI, File, UploadFile
import whisper
import pyttsx3

app = FastAPI()
model = whisper.load_model("base")
tts = pyttsx3.init()

@app.post("/voice")
async def process_voice(file: UploadFile = File(...)):
    audio = await file.read()
    with open("temp.wav", "wb") as f:
        f.write(audio)
    result = model.transcribe("temp.wav")
    tts.say(result["text"])
    tts.runAndWait()
    return {"text": result["text"]}
