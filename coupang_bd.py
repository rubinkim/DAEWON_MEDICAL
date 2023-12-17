#-*- coding: utf-8 -*-

host = "brd.superproxy.io:22225"
user_name = "brd-customer-hl_878d4fe7-zone-unblocker"
password = "ma5cz45h7cnv"

# 위의 정보들을 이용해서 proxy_url을 만든다.
proxy_url = f"https://{user_name}:{password}@{host}"
print(proxy_url)