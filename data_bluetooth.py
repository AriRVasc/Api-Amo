import requests
import json

# Nome do arquivo JSON na sua pasta
json_file_path = "sensor.json"

# Lê o conteúdo do arquivo JSON
with open(json_file_path, "r") as file:
    received_json = json.load(file)


# URL da rota da sua API
api_url = "http://127.0.0.1:8000/receive_bluetooth_data"  # Substitua pelo endereço da sua API

# Cabeçalhos para a requisição (se necessário)
headers = {"Content-Type": "application/json"}

# Faz a requisição POST com o JSON recebido
response = requests.post(api_url, data=json.dumps(received_json), headers=headers)

# Verifica a resposta da API
if response.status_code == 200:
    print("JSON enviado com sucesso para a API!")
else:
    print("Erro ao enviar o JSON para a API:", response.status_code)
