import pandas as pd
import ta
import yfinance as yf

"""
There are numerous candlestick patterns used in technical analysis. Here are a few commonly recognized candlestick patterns:

Doji: This pattern occurs when the opening and closing prices are very close or equal, resulting in a small or no real body. It suggests indecision in the market.

Hammer: It has a small real body near the top end of the trading range, with a long lower shadow. It indicates a potential bullish reversal after a downtrend.

Shooting Star: The opposite of the hammer pattern, it has a small real body near the bottom end of the trading range, with a long upper shadow. It suggests a potential bearish reversal after an uptrend.

Engulfing Pattern: It consists of two candlesticks where the body of the second candlestick completely engulfs the body of the first. A bullish engulfing pattern occurs at the end of a downtrend and suggests a potential reversal. A bearish engulfing pattern occurs at the end of an uptrend and suggests a potential reversal.

Morning Star: It is a three-candle pattern. The first candlestick is a large bearish candle, followed by a small-bodied candlestick that gaps down, and finally a large bullish candle that closes within the body of the first candle. It signals a potential bullish reversal.

Evening Star: It is the opposite of the morning star pattern. It starts with a large bullish candle, followed by a small-bodied candlestick that gaps up, and ends with a large bearish candle that closes within the body of the first candle. It indicates a potential bearish reversal.

These are just a few examples of candlestick patterns. There are many more patterns, including the Hanging Man, Piercing Pattern, Harami, Three White Soldiers, and Three Black Crows, among others. Each pattern carries its own interpretation and significance in the context of market sentiment and price actio
"""


# Download data from Yahoo Finance
symbol = "AAPL"  # Example stock symbol (Apple Inc.)
start_date = "2022-01-01"  # Example start date
end_date = "2022-12-31"  # Example end date

data = yf.download(symbol, start=start_date, end=end_date)

# Calculate candlestick patterns

# Calculate candlestick patterns
data['CDL_DOJI'] = 0
data['CDL_HAMMER'] = 0

for i in range(len(data)):
    # Doji pattern
    if abs(data['Close'][i] - data['Open'][i]) <= 0.1 * (data['High'][i] - data['Low'][i]):
        data['CDL_DOJI'][i] = 1

    # Hammer pattern
    if (data['Close'][i] - data['Low'][i]) > 2 * (data['High'][i] - data['Close'][i]):
        data['CDL_HAMMER'][i] = 1

# Print the candlestick patterns
print(data[['Date', 'Open', 'High', 'Low', 'Close', 'CDL_DOJI', 'CDL_HAMMER']])

# Add more candlestick patterns as needed

# Print the candlestick patterns
print(data[['Open', 'High', 'Low', 'Close', 'CDL_DOJI', 'CDL_HAMMER']])
