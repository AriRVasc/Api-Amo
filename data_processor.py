# Importação da classe BluetoothData do módulo models
from models import BluetoothData

# Definição da classe DataProcessor
class DataProcessor:
    def __init__(self):
        self.data_by_id = {}  # Dicionário para armazenar dados de temperatura por ID

    # Método para processar os dados recebidos
    def process_data(self, data: BluetoothData):
        if data.id not in self.data_by_id:  # Se o ID não estiver no dicionário
            self.data_by_id[data.id] = data.temperature  # Adiciona o ID e a temperatura ao dicionário
        else:  # Se o ID já estiver no dicionário
            self.data_by_id[data.id] = data.temperature  # Atualiza a temperatura associada ao ID

    # Método para obter a temperatura a partir de um ID
    def get_temperature(self, id):
        return self.data_by_id.get(id)  # Retorna a temperatura associada ao ID ou None se o ID não estiver presente
