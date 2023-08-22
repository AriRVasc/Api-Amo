from fastapi import FastAPI
from models import BluetoothData
from data_processor import DataProcessor

app = FastAPI()
data_processor = DataProcessor()

@app.post('/receive_bluetooth_data')
async def receive_bluetooth_data(data: BluetoothData):
    data_processor.process_data(data)
    return {"message": "Dados recebidos com sucesso"}

@app.get('/get_temperature/{id}')
async def get_temperature(id: int):
    temperature = data_processor.get_temperature(id)
    if temperature is not None:
        return {"id": id, "temperature": temperature}
    else:
        return {"message": "Sem dados de temperatura para o ID fornecido"}
