import urllib.request
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
import datetime

print(datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

shops = []

for i in range(1, 51):
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store='
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        shop_name = tds[1].string
        shop_address = tds[3].string
        shop_phone = tds[5].string

        shops.append([shop_name]+[shop_address]+[shop_phone]+[datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")])

#print(shops)
hollys_df = pd.DataFrame(shops, columns=('매장이름', '주소', '전화번호', '일시'))
hollys_df.to_csv('hollys.csv', mode='w', encoding='cp949')