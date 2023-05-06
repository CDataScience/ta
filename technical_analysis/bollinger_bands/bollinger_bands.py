import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import yfinance as yf
import matplotlib.pyplot as plt

# Configurar la API key de Alpha Vantage
#key = 'D81XVUS9S81BVIPW'

# Crear una instancia de TimeSeries con la API key de Alpha Vantage
#ts = TimeSeries(key, output_format='pandas')

# Descargar los datos de cotización de Banco Santander (SAN.MC) desde Alpha Vantage
#data, meta_data = ts.get_daily_adjusted(symbol='TSCO.LON')
# Renombrar las columnas de los datos de cotización de bolsa
#data = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. adjusted close': 'Adj Close', '6. volume': 'Volume', '7. dividend amount': 'Dividend Amount', '8. split coefficient': 'Split Coefficient'})

# Descargar los datos de cotización de bolsa de Banco Santander (SAN.MC) desde Yahoo Finance
data = yf.download("SAN.MC", start="2020-01-01", end="2022-12-31")

data.to_csv('cotizaciones.csv')
# Calcular la media móvil y la desviación estándar
data['MA20'] = data['Close'].rolling(window=20).mean()
data['std20'] = data['Close'].rolling(window=20).std()

# Calcular las bandas de Bollinger
data['upper'] = data['MA20'] + 2 * data['std20']
data['lower'] = data['MA20'] - 2 * data['std20']

# Visualizar las bandas de Bollinger en un gráfico
WIDTH_SIZE=100
HEIGHT_SIZE=100
plt.figure(figsize=(WIDTH_SIZE,HEIGHT_SIZE))
plt.plot(data['Close'])
plt.plot(data['MA20'])
plt.plot(data['upper'])
plt.plot(data['lower'])
plt.show(block=True)
