import requests
url='https://www.binance.com/en/blog/ecosystem/421499824684903685'
r=requests.get(url)
print(r.text)