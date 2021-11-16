from bs4 import BeautifulSoup
import requests

url = f'https://cafe.naver.com/dokchi/menu/5366'
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
title = soup.select("a#article")[0].text
print(title)
