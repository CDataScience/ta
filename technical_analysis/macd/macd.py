import pandas as pd
import numpy as np
import ta
import yfinance as yf

# Descargar los datos de cotización de bolsa de Banco Santander (SAN.MC) desde Yahoo Finance
data = yf.download("SAN.MC", start="2020-01-01", end="2022-12-31")

data.to_csv('cotizaciones.csv')

# Calculate Moving Averages (SMA and EMA)
data['SMA'] = ta.trend.sma_indicator(data['Close'], window=20)
data['EMA'] = ta.trend.ema_indicator(data['Close'], window=20)

# Calculate RSI
data['RSI'] = ta.momentum.rsi(data['Close'], window=14)

# Calculate MACD
macd = ta.trend.MACD(data['Close'])
data['MACD'] = macd.macd()
data['Signal Line'] = macd.macd_signal()



# Calculate Bollinger Bands
data['BB_upper'], data['BB_middle'], data['BB_lower'] = ta.volatility.bollinger_hband_indicator(data['Close'], window=20, window_dev=2), ta.volatility.bollinger_mband_indicator(data['Close'], window=20), ta.volatility.bollinger_lband_indicator(data['Close'], window=20, window_dev=2)

# Calculate Stochastic Oscillator
data['%K'], data['%D'] = ta.momentum.stoch(data['High'], data['Low'], data['Close'], window=14), ta.momentum.stoch_signal(data['High'], data['Low'], data['Close'], window=14, smooth_window=3)

# Calculate Fibonacci Retracement
data['Fibonacci 0.382'] = data['Close'] * 0.382
data['Fibonacci 0.618'] = data['Close'] * 0.618
data['Fibonacci 1.000'] = data['Close']
data['Fibonacci 1.382'] = data['Close'] * 1.382
data['Fibonacci 1.618'] = data['Close'] * 1.618


# Print the calculated indicators
print(data[['Date', 'SMA', 'EMA', 'RSI', 'MACD', 'Signal Line']])

# You can also save the calculated indicators to a new CSV file if needed
#data.to_csv('path/to/save/indicators.csv', index=False)
