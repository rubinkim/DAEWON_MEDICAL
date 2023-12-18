#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import warnings
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = "brd.superproxy.io:22225"
user_name = "brd-customer-hl_878d4fe7-zone-unblocker"
password = "ma5cz45h7cnv"


proxy_url = f"https://{user_name}:{password}@{host}"
print(proxy_url)

proxies = {"http": proxy_url, "https": proxy_url}
keyword = input("ê²??ƒ‰?•  ? œ?’ˆ ?ž…? ¥ : ")

link_list = []
for page_num in range(1, 3):      
    print(f"<<<<< ?Ž˜?´ì§? {page_num} >>>>>")
    url = f"https://www.coupang.com/np/search?q={keyword}&page={page_num}&listSize=72"
    print(f"url : {url}")         
    print()

    response = requests.get(url, proxies=proxies, verify=False)    
    html = response.text
    #print(html[:1000])
    soup = BeautifulSoup(html, "html.parser")
    
    items = soup.select("[class=search-product]")                               
    print(len(items))

    for item in items:
        name = item.select_one(".name").text                         
        price = item.select_one(".price-value")
        if not price:                                               
            continue
        link = f"https://coupang.com{item.a['data-product-link']}"
        link_list.append(link)
        
        print(f"{name} : {price.text}")                              
        print(link)
        print()
        
print(link_list)
print(len(link_list))