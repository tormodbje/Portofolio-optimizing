import yfinance as yf

ticker = yf.Ticker("AAPL")
data = ticker.history(period="1d", interval="1h")  # Siste dag, 1-minutts intervaller

print(data[["Close"]])