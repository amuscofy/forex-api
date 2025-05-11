from fastapi import FastAPI, HTTPException
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
    signals = []
    for pair in pairs:
        try:
            # Try to get the signal for each pair
            signal_data = get_signal(pair)
            signals.append(signal_data)
        except Exception as e:
            # If there's an error (e.g., network issue or Yahoo Finance failure), handle it gracefully
            signals.append({
                "pair": pair,
                "signal": "Error",
                "message": str(e)  # Provide the error message in the response
            })
    return signals
