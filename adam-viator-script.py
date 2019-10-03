# encoding=utf8
import requests, re
from bs4 import BeautifulSoup

tours = []
url = 'https://www.viator.com/Ireland/d56-ttd'
iter = True
i = 1
while (iter):
    if (i == 1):
        r = requests.get(url)
    else:
        print(url + '/' + str(i))
        r = requests.get(url + '/' + str(i))
    i += 1

    soup = BeautifulSoup(r.text, "html.parser")
    #print (str(r.status_code) + ' - ' + str(i))
    if (r.status_code != 404):
        tours.append(soup.find_all(attrs={'data-action-tag':'view_product'}))
    else:
        iter = False

print (len(tours))
with open('index.html', 'w+') as f:
    f.seek(0)
    for tour in enumerate(tours):
        for t in tour:
            try:
                f.write(BeautifulSoup((str(t)).encode('ascii', 'ignore').decode('ascii'), 'html.parser').prettify())
            except Exception as e:
                print(e)
