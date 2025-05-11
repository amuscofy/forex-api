import yfinance as yf
import pandas_ta as ta
import datetime

def get_signal(symbol="EURUSD=X"):
    # Check if it's a weekend (Saturday or Sunday)
    today = datetime.datetime.now()
    if today.weekday() >= 5:  # Saturday or Sunday
        return {"pair": symbol, "signal": "No data - Weekend", "rsi": None, "macd": None}

    try:
        # Fetch data from Yahoo Finance
        df = yf.download(symbol, period="30d", interval="1h")
        
        # Check if the data is empty or has insufficient data
        if df.empty or len(df) < 30:
            return {"pair": symbol, "signal": "No data", "rsi": None, "macd": None}

        # Calculate the RSI and MACD indicators
        df["RSI"] = ta.rsi(df["Close"], length=14)
        macd = ta.macd(df["Close"])
        df["MACD"] = macd["MACDh_12_26_9"]

        # Get the last row of data
        last = df.iloc[-1]
        signal = "Hold"

        # Generate signal based on RSI and MACD values
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

    except Exception as e:
        # Return an error message in case of failure
        return {"pair": symbol, "signal": "Error", "message": str(e)}
