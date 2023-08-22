from pydantic import BaseModel

class BluetoothData(BaseModel):
    id: int
    temperature: float
