from bs4 import BeautifulSoup
import requests

def getPrice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/41.0.2228.0 Safari/537.36'}
    res = requests.get(url, headers=headers)

    if res.raise_for_status() == None:
        soup = BeautifulSoup(res.text, 'html.parser')
        price = soup.find('h2', class_='K6KjbGieCG')
        return price.text.strip()

price = getPrice('''https://www.carousell.sg/p/
        corsair-4000d-tempered-glass-mid-tower-atx-pc-case-non-led-120mm-fans-x-2-
        included-white-or-black-1044966059/''')
print('The price is ' + str(price))