# Import necessary libraries
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
import matplotlib.pyplot as plt

# Set up Alpha Vantage API key (commented out)
#key = 'D81XVUS9S81BVIPW'

# Create a TimeSeries instance with Alpha Vantage API key (commented out)
#ts = TimeSeries(key, output_format='pandas')

# Download daily adjusted stock quote data for Banco Santander (SAN.MC) from Alpha Vantage (commented out)
#data, meta_data = ts.get_daily_adjusted(symbol='TSCO.LON')

# Rename stock quote data columns
#data = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. adjusted close': 'Adj Close', '6. volume': 'Volume', '7. dividend amount': 'Dividend Amount', '8. split coefficient': 'Split Coefficient'})

# Download stock quote data for Banco Santander (SAN.MC) from Yahoo Finance
data = yf.download("SAN.MC", start="2020-01-01", end="2022-12-31")

# Save stock quote data to CSV file
data.to_csv('cotizaciones.csv')

# Calculate moving average and standard deviation
data['MA20'] = data['Close'].rolling(window=20).mean()
data['std20'] = data['Close'].rolling(window=20).std()

# Calculate Bollinger Bands
data['upper'] = data['MA20'] + 2 * data['std20']
data['lower'] = data['MA20'] - 2 * data['std20']

# Plot Bollinger Bands on a chart
WIDTH_SIZE=100
HEIGHT_SIZE=100
plt.figure(figsize=(WIDTH_SIZE,HEIGHT_SIZE))
plt.plot(data['Close'])
plt.plot(data['MA20'])
plt.plot(data['upper'])
plt.plot(data['lower'])
plt.show(block=True)
