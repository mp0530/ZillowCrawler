import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://www.zillow.com/',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'refer': 'https://www.zillow.com/homes/Austin,-TX_rb/'
}

response = requests.get('https://www.zillow.com/homes/Austin,-TX_rb/', headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
result_count_span = soup.find('span', class_ ='result-count')
print(result_count_span)
count = (result_count_span.text.split()[0].replace(",", ""))
print(datetime.now().hour)
with open("D:\python\zillow_austin.txt", "a") as w:
    w.write('\n' + str(date.today()) + '; ' + str(datetime.now().hour) + "; " + count)