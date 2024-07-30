from abc import ABC, abstractmethod
from pandas import DataFrame
from persistence import data_persistence as dp

class Indicator(ABC):
    def __init__(self, name: str, data: DataFrame):
        self.data = data
        self.name = name
        
    @abstractmethod
    def run(self):
        pass
    
    def persist(self, persistence_type:str):
        if persistence_type == "file":
            self.data.to_csv(f"data/{self.name}.csv", index=False)
        elif persistence_type == "database":
            # Conectar a la base de datos Postgres y insertar los datos de cotización
            data_persistence = dp.DataPersistence()
            data_persistence.insert_data(self.data)
            data_persistence.close_conn()