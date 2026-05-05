import requests


BASE_URL = "https://gym-api-08pc.onrender.com"

def get(endpoint, head):
    response = requests.get(f'{BASE_URL}{endpoint}', headers=head)
    response.raise_for_status()
    return response.json()

def post(endpoint, data, head):
    response = requests.post(f'{BASE_URL}{endpoint}', json=data, headers=head)
    response.raise_for_status()
    return  response.json()

