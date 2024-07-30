import pandas as pd
import mplfinance as mpf
from ta.momentum import RSIIndicator

# Load data
df = pd.read_csv('cotizaciones.csv', index_col='Date', parse_dates=True)

# Calculate RSI
rsi_indicator = RSIIndicator(df['Close'], window=14)
df['RSI'] = rsi_indicator.rsi()

# Create a new DataFrame for the RSI plot
rsi = df[['RSI']]

# Plot with mplfinance
mpf.plot(
    df,
    type='candle',
    volume=True,
    addplot=mpf.make_addplot(rsi, panel=1, color='g'),
    panel_ratios=(6, 2)  # Adjust panel ratios as needed
)