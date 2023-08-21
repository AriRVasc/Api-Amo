# Importação das bibliotecas necessárias
import requests  # Para fazer requisições HTTP
import json  # Para trabalhar com JSON

# Nome do arquivo JSON na pasta
json_file_path = "sensor.json"  # Define o caminho para o arquivo JSON a ser lido

# Lê o conteúdo do arquivo JSON
with open(json_file_path, "r") as file:
    received_json = json.load(file)  # Carrega o conteúdo do arquivo JSON em um dicionário Python

# URL da API
api_url = "http://127.0.0.1:8000/receive_bluetooth_data" 

# Cabeçalhos para a requisição 
headers = {"Content-Type": "application/json"}  # Define os cabeçalhos da requisição, especificamente o tipo de conteúdo

# Faz a requisição POST com o JSON recebido
response = requests.post(api_url, data=json.dumps(received_json), headers=headers)  # Envia a requisição POST com o JSON serializado

# Verifica a resposta da API
if response.status_code == 200:
    print("JSON enviado com sucesso para a API!")  # Mensagem de sucesso se a resposta da API for 200
else:
    print("Erro ao enviar o JSON para a API:", response.status_code)  # Mensagem de erro com o código de status da resposta da API
