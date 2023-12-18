#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import warnings
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

host = "brd.superproxy.io:22225"
user_name = "brd-customer-hl_878d4fe7-zone-unblocker"
password = "ma5cz45h7cnv"

# ���� �������� �̿��ؼ� proxy_url�� �����.
proxy_url = f"https://{user_name}:{password}@{host}"
print(proxy_url)

proxies = {"http": proxy_url, "https": proxy_url}
keyword = input("�˻��� ��ǰ �Է� : ")
#url = f"https://www.coupang.com/np/search?component=&q={keyword}"

for page_num in range(1, 5):
    url = f"https://www.coupang.com/np/search?q={keyword}&page={page_num}&listSize=72"

    response = requests.get(url, proxies=proxies, verify=False)     # verify = False�� �־��ָ� ssl���������� �����ϱ� ������ ������ �߻����� �ʴ´�.
    html = response.text
    #print(html[:1000])
    soup = BeautifulSoup(html, "html.parser")
    #items = soup.select(".search-product.search-product__ad-badge") # class �̴ϱ� .�� �տ� �����. �׸��� search-product search-product__ad-badge�� ��ĭ�� .���� �ٲپ�� �Ѵ�.
                                                                    # ��ȭ�鿡 36���� ����� �Ǿ� �ִµ� 59���� ���Դ�. ������ 36�̴�. �� ����?

    items = soup.select("[class=search-product]")                    # �������� 27���� ���Դ�.            
    print(len(items))

    for item in items:
        name = item.select_one(".name").text                         # select�� �̿��ϸ� list�� return�ϹǷ� �ٽ� [0]�� ���� �۾��� ����� �ϴµ� select_one�� value�� return�Ѵ�.
        price = item.select_one(".price-value")
        if not price:                                                # �߰���ǰ�� ��쿡�� price.value��� class�� �����Ƿ� .text�� �Ⱥ��̸� ������ �߻��ϴ� ��� none�� ��ȯ�Ѵ�.
            continue
        link = f"https://coupang.com{item.a['data-product-link']}"
        print(f"{name} : {price.text}")                              # ũ�Ѹ��� �� ���� ������� �ٸ��� ���´�.
        print(link)
        print()