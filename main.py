import yfinance as yf
from persistence import insert_stock_history, connect_db

# Descargar los datos de cotización de Yahoo Finance
msft = yf.Ticker("MSFT")
data = msft.history(period="max")

# Conectar a la base de datos Postgres y insertar los datos de cotización
conn = connect_db()
insert_stock_history(conn, data)
conn.close()