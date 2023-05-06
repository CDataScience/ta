import psycopg2
import yfinance as yf

# Función para conectar a la base de datos Postgres
def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="my_database",
        user="my_user",
        password="my_password"
    )
    return conn

# Función para insertar los datos de cotización en la tabla correspondiente
def insert_stock_history(conn, data):
    cur = conn.cursor()
    for index, row in data.iterrows():
        cur.execute("""
            INSERT INTO stock_history (date, open, high, low, close, volume, dividends, stock_splits)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Dividends'], row['Stock Splits']))
    conn.commit()
    cur.close()


