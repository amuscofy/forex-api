# main.py

from fastapi import FastAPI
from signal_generator import get_signal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS config for React Native frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/signals")
def daily_signals():
    pairs = ["EURUSD=X", "GBPUSD=X", "USDJPY=X"]
    return [get_signal(pair) for pair in pairs]
