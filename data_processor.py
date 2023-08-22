from models import BluetoothData

class DataProcessor:
    def __init__(self):
        self.data_by_id = {}

    def process_data(self, data: BluetoothData):
        if data.id not in self.data_by_id:
            self.data_by_id[data.id] = data.temperature
        else:
            self.data_by_id[data.id] = data.temperature

    def get_temperature(self, id):
        return self.data_by_id.get(id)
