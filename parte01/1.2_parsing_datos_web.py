import requests
import feedparser

url = 'https://github.com/robin-dev-git/curso-python'

respuesta = requests.get(url)
print(respuesta.status_code)