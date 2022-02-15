import requests
import feedparser

url = ''

respuesta = requests.get(url)
print(respuesta.status_code)