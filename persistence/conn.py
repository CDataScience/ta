import psycopg2
import json

class PostgresConnector:

    def __init__(self):
        self.db_params = self.get_params()

    def get_params():
        # Load database connection parameters from JSON file
        with open('db_params.json') as json_file:
            db_params = json.load(json_file)
        


    # Función para conectar a la base de datos Postgres
    def connect_db(self):
        try:
            conn = psycopg2.connect(**self.db_params)
            return conn
        except psycopg2.Error as e:
            print(f"Error: {e}")


    def close_conn(self):
        self.conn.close()
