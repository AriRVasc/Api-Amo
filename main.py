from fastapi import FastAPI, HTTPException
#classe do framework FastAPI que representa a aplicação web. 
# Ela é usada para criar rotas e definir as operações que a aplicação suportará.
#É uma classe do FastAPI que permite lançar exceções HTTP personalizadas. 


from cachetools import TTLCache
import uvicorn

app = FastAPI()

# Criação de um objeto TTLCache para armazenar os dados em cache
# maxsize define o número máximo de entradas em cache, ttl define o tempo de vida em segundos
cache = TTLCache(maxsize=100, ttl=300)  # Armazena até 100 entradas com tempo de vida de 300 segundos (5 minutos)

# Dicionário vazio para armazenar as temperaturas recebidas de diferentes microcontroladores
temperaturas = {}

# Definição da rota que aceita solicitações POST para '/temperatura'
@app.post('/temperatura')
def receber_temperatura(dados: dict):
    microcontrolador_id = dados.get('microcontrolador_id')
    temperatura = dados.get('temperatura')

    if microcontrolador_id is None or temperatura is None:
        raise HTTPException(status_code=400, detail='Dados incompletos')

    # Armazenamento da temperatura associada ao ID do microcontrolador no dicionário
    temperaturas[microcontrolador_id] = temperatura

    # Armazenamento dos dados no cache, usando o ID do microcontrolador como chave
    cache[microcontrolador_id] = temperatura

    # Resposta com mensagem de sucesso em formato JSON
    return {'message': 'Dados de temperatura recebidos com sucesso!'}

# Definição da rota que aceita solicitações GET para '/temperaturas'
@app.get('/temperaturas')
def listar_temperaturas():
    # Criação de uma cópia dos dados em cache e conversão para um dicionário
    cache_data = dict(cache)
    # Retorno dos dados em cache em formato JSON
    return cache_data

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
