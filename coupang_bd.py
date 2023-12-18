#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import warnings
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = "brd.superproxy.io:22225"
user_name = "brd-customer-hl_878d4fe7-zone-unblocker"
password = "ma5cz45h7cnv"

# 위의 정보들을 이용해서 proxy_url을 만든다.
proxy_url = f"https://{user_name}:{password}@{host}"
print(proxy_url)

proxies = {"http": proxy_url, "https": proxy_url}
keyword = input("검색할 제품 입력 : ")
url = f"https://www.coupang.com/np/search?component=&q={keyword}"
response = requests.get(url, proxies=proxies, verify=False)     # verify = False를 넣어주면 ssl인증과정을 생략하기 때문에 에러가 발생하지 않는다.
html = response.text
#print(html[:1000])
soup = BeautifulSoup(html, "html.parser")
#items = soup.select(".search-product.search-product__ad-badge") # class 이니까 .을 앞에 찍었다. 그리고 search-product search-product__ad-badge는 빈칸을 .으로 바꾸어야 한다.
                                                                 # 한화면에 36개씩 보기로 되어 있는데 59개가 나왔다. 선생은 36이다. 왜 나만?

items = soup.select("[class=search-product]")                    # 이제서야 27개가 나왔다.            
print(len(items))

for item in items:
    name = item.select_one(".name").text                         # select를 이용하면 list를 return하므로 다시 [0]와 같은 작업을 해줘야 하는데 select_one은 value를 return한다.
    price = item.select_one(".price-value")
    if not price:                                                # 중고제품인 경우에는 price.value라는 class가 없으므로 .text를 안붙이면 에러가 발생하는 대신 none을 반환한다.
        continue
    link = f"https://coupang.com{item.a['data-product-link']}"
    print(f"{name} : {price.text}")                              # 크롤링할 때 마다 결과값이 다르게 나온다.
    print(link)
    print()
    
"""
https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&
eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&
filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&
page=3&rocketAll=false&searchIndexingToken=1=9&backgroundColor=
"""
# 위에서 %EB%85%B8%ED%8A%B8%EB%B6%81부분이 노트북임은 아래에서 확인할 수 가 있다.
# https://www.coupang.com/np/search?q=노트북&channel=recent
# https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent
# 위url중 페이지가 3이라고 알 수 있는 부분은 url중 맨아랫줄에 page=3라는 부분이 있다.
# 나머지는 다 필요가 없고 검색어와 페이지만 url에서 아래와 같이 뽑는다.
# https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&page=3
# 이렇게 변경한 url이 잘 작동하는지 알아보기 위해 page를 7로 바꿔서 불러보자.
# https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&page=7
# 해봤더니 page7로 변경되서 원하는 페이지에 이동해 있는 것을 알 수 있다.

# 이제 다음 이슈는 가능한한 많은 제품을 가져오는게 목적이므로 36개씩보기에서 72개씩보기로 변경해보자.