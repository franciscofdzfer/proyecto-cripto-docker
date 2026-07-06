import requests
from app.config import API_URL

def obtener_precios():
    response = requests.get(API_URL)
    return response.json()
