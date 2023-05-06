import pandas as pd
import ta
import yfinance as yf

# Descargar los datos de cotización de bolsa de Banco Santander (SAN.MC) desde Yahoo Finance
data = yf.download("SAN.MC", start="2020-01-01", end="2022-12-31")

# Identify the Head and Shoulders pattern
data['Left Shoulder'] = data['High'].rolling(window=5).max()
data['Head'] = data['High'].rolling(window=5, center=True).max()
data['Right Shoulder'] = data['High'].rolling(window=5, center=False).max()

# Find the potential neckline
neckline = (data['Left Shoulder'] + data['Right Shoulder']) / 2

# Identify the pattern by checking for specific conditions
pattern_indices = []
for i in range(len(data)):
    if i < 2 or i >= len(data) - 2:
        continue
    if (
        data['Head'][i - 1] > data['Head'][i - 2]
        and data['Head'][i - 1] > data['Head'][i]
        and data['Left Shoulder'][i] < data['Left Shoulder'][i - 1]
        and data['Left Shoulder'][i] < data['Left Shoulder'][i - 2]
        and data['Right Shoulder'][i] < data['Right Shoulder'][i + 1]
        and data['Right Shoulder'][i] < data['Right Shoulder'][i + 2]
        and data['Low'][i] < neckline[i]
    ):
        pattern_indices.append(i)

# Print the identified pattern indices
print("Pattern Indices:", pattern_indices)
