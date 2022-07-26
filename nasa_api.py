def lambda_handler(event, context):
  # importando as bibliotecas
  import requests
  import pandas as pd
  import os

  # pego o token de acesso definido como variavel de ambiente
  def auth():
    api_key = os.environ.get("API_KEY")
    return api_key
  

  # crio a url da requisição
  def cria_url(api_key):
    lon = -95.33
    lat = 29.78
    date = '2018-01-01'
    url = f'https://api.nasa.gov/planetary/earth/assets?lon={lon}&lat={lat}&date={date}&api_key={api_key}'
    return url

  # faz a requiaição
  def faz_request(url):
    response = requests.get(url)
    return response

  # executo as funções anteriores
  def main():
    api_key = auth()
    url = cria_url(api_key)
    response = faz_request(url)
    return response.json()

  # normalizo o json da resposta para deixar colunar
  def normaliza_dados(resp):
    return pd.json_normalize(resp, sep='_')


  response = main()
  df = normaliza_dados(response)
  print("Function exection ended")

