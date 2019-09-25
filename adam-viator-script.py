import requests
import time
from bs4 import BeautifulSoup

tours = []
url = 'https://www.viator.com/Ireland/d56-ttd'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
tours.append(soup.findAll('div', {'class', 'product-card'}))

print(tours)
