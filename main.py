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
    # Add BTCUSD=X and ETHUSD=X to the list of pairs
    pairs = ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "BTCUSD=X", "ETHUSD=X"]
    signals = []
    
    # Loop through each pair and get the signal, catching any exceptions
    for pair in pairs:
        try:
            # Try to get the signal for each pair
            signal_data = get_signal(pair)
            signals.append(signal_data)
        except Exception as e:
            # If an error occurs, append an error message
            signals.append({
                "pair": pair,
                "signal": "Error",
                "message": str(e)
            })
    
    return signals
