# Importação da classe BaseModel da biblioteca Pydantic
from pydantic import BaseModel

# Definição da classe BluetoothData que herda da classe BaseModel
class BluetoothData(BaseModel):
    id: int  # Campo para armazenar um valor inteiro (ID)
    temperature: float  # Campo para armazenar um valor de ponto flutuante (temperatura)
