import bs4
import requests

# Amazon does not allow web scraping.

def getPrice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/41.0.2228.0 Safari/537.36'}
    res = requests.get(url, headers=headers)

    if res.raise_for_status() == None:
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        element = soup.select('#main > div > div._1Bj1VS > div.page-product > div.container > div.product-briefing.flex.card._2cRTS4 > div.flex.flex-auto.k-mj2F > div > div:nth-child(3) > div > div > div > div > div > div')
        price = element[0].text.strip()

        return price

price = getPrice('''https://shopee.sg/%F0%9F%87%B8%F0%9F%87%AC%F0%9F%94%
        A5Ready-Stock%F0%9F%94%A5Wood-Parallettes-Handstand-Pushups-Stands-Bars-
        Gymnastic-Russian-Style-Stretch-Push-Ups-Double-Rod-i.181654948.5932438192''')
print('The price is ' + price)