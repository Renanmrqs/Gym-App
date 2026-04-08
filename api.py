import requests

BASE_URL = "https://web-production-7fb8d2.up.railway.app"

def get(endpoint):
    response = requests.get(f'{BASE_URL}{endpoint}')
    response.raise_for_status()
    return response.json()

def post(endpoint, data):
    response = requests.post(f'{BASE_URL}{endpoint}', json=data)
    response.raise_for_status()
    return  response.json()