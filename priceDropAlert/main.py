import requests
from bs4 import BeautifulSoup

target_url = 'https://www.amazon.com/dp/B084CT21P8/ref=twister_B087HH6DJW?th=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

while True:
    try:
        data = requests.get(target_url, headers=headers).text
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find(name='span',id="price_inside_buybox", class_="a-size-medium a-color-price")
        price = price.get_text().split('\n')[1]
    except AttributeError:
        print('Trying again')
    else:
        break

price = float(price.split('$')[1])
print(price)
threshold_price = 130.00
if price<=threshold_price:
    print('Yeah!!')