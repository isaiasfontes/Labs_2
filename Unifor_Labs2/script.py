import os
from dotenv import load_dotenv
import requests
import json


# Load environment variables from .env file
load_dotenv()



# esse link pode mudar se os donos da API mudarem
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes_dic = cotacoes.json()

# Access environment variables
moeda = os.getenv("MOEDA")
bid = os.getenv("bid")

cotacoes_dolar = cotacoes_dic["{moeda}"]["{bid}"]
print(cotacoes_dolar)


# Access environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

# Use the environment variables in your code
print(f"API Key: {api_key}")
print(f"Database URL: {database_url}")
