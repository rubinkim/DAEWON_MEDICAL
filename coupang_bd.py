#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

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
print(html[:1000])