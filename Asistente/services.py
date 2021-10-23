import requests

API_URL = 'https://apipruebamadison.herokuapp.com/'

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def obtener_usuario(params={}):
    response = generate_request(API_URL+'usuarios/', params)

    if response:
        usuario = response.get('usuarios')[0]
        return usuario.get('nombre').get('apellido')