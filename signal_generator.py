# signal_generator.py

import yfinance as yf
import pandas_ta as ta

def get_signal(symbol="EURUSD=X"):
    df = yf.download(symbol, period="30d", interval="1h")
    if df.empty or len(df) < 30:
        return {"pair": symbol, "signal": "No data", "rsi": None, "macd": None}

    df["RSI"] = ta.rsi(df["Close"], length=14)
    macd = ta.macd(df["Close"])
    df["MACD"] = macd["MACDh_12_26_9"]

    last = df.iloc[-1]
    signal = "Hold"

    if last["RSI"] < 30 and last["MACD"] > 0:
        signal = "Buy"
    elif last["RSI"] > 70 and last["MACD"] < 0:
        signal = "Sell"

    return {
        "pair": symbol.replace("=X", ""),
        "signal": signal,
        "rsi": round(last["RSI"], 2),
        "macd": round(last["MACD"], 2),
        "timestamp": str(df.index[-1])
    }
