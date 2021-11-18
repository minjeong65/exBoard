from bs4 import BeautifulSoup
import requests


# 제목 크롤링
# title=[]
# for n in range(1,5):
#     url = f'https://terms.naver.com/list.naver?cid=58779&categoryId=58779&so=st1.dsc&viewType=&categoryType=&page={n}'
#     res = requests.get(url)
#     soup = BeautifulSoup(res.text, "lxml")

#     for i in range(15):
#         site = soup.select("ul>li>div>div>strong")[i].text
#         site = site.split('-')
#         title.append(site[0].replace('\n',""))

# print(title)

# 제목 링크 크롤링
urls=[] 
for n in range(1,5):
    url = f'https://terms.naver.com/list.naver?cid=58779&categoryId=58779&so=st1.dsc&viewType=&categoryType=&page={n}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    
    for href in soup.find("ul", class_="content_list").find_all("li"): #ul의 content_list 중 모든 li를 찾음
        site = href.find("a")["href"]
        if '/' in site:
            urls.append(site)


title = []
for i in urls:
    url = f'https://terms.naver.com{i}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    mu = soup.select("h2.headword")[0].text #뮤지컬 제목
    title.append(mu)

# for i in title:
#     b = Board(subject = i).save()