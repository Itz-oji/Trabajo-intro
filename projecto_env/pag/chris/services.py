import requests

def generar_request(url, params={}):
    response= requests.get(url , params=params)
    if response.status_code == 200:
        return response.json()

def get_fotoperro(params={}):
    response= generar_request('https://dog.ceo/api/breeds/image/random', params)
    if response:
        imagen= response.get('message')
        return imagen
    return ''

def get_fotogato(params={}):
    response= generar_request('https://api.thecatapi.com/v1/images/search', params)
    if response:
        imagen= response.get('url')
        return imagen
    return ""

