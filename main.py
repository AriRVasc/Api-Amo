# Importação da classe FastAPI do módulo fastapi
from fastapi import FastAPI

# Importação da classe BluetoothData do módulo models
from models import BluetoothData

# Importação da classe DataProcessor do módulo data_processor
from data_processor import DataProcessor

# Criação de uma instância da classe FastAPI
app = FastAPI()

# Criação de uma instância da classe DataProcessor
data_processor = DataProcessor()

# Definição de rota POST para o endpoint '/receber_dados_bluetooth'
@app.post('/receber_dados_bluetooth')
async def receber_dados_bluetooth(data: BluetoothData):
    data_processor.process_data(data)  # Chama o método process_data da instância de DataProcessor
    return {"message": "Dados recebidos com sucesso"}  # Retorna uma mensagem de sucesso

# Definição de rota GET para o endpoint '/get_temperature/{id}'
@app.get('/get_temperature/{id}')
async def get_temperature(id: int):
    temperature = data_processor.get_temperature(id)  # Chama o método get_temperature da instância de DataProcessor
    if temperature is not None:
        return {"id": id, "temperature": temperature}  # Retorna um JSON com o ID e a temperatura
    else:
        return {"message": "Sem dados de temperatura para o ID fornecido"}  # Retorna uma mensagem se não houver temperatura para o ID

