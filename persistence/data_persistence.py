import psycopg2
from conn import PostgresConnector
class DataPersistence:

    def __init__(self):
        self.conn = PostgresConnector()
        
    # Función para insertar los datos de cotización en la tabla correspondiente
    def insert_stock_history(self, data):
        cur = self.conn.cursor()
        for index, row in data.iterrows():
            cur.execute("""
                INSERT INTO stock_history (date, open, high, low, close, volume, dividends, stock_splits)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'], row['Dividends'], row['Stock Splits']))
        self.conn.commit()
        cur.close()
    
    
    def close_conn(self):
        self.conn.close()
