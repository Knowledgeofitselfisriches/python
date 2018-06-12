import urllib.request
	
response = urllib.request.urlopen('https://www.baidu.com')
print(response.status)
# print(response.read().decode("utf-8"))
import requests
resp = requests.get("http://www.baidu.com",prams=dicts)
print(resp.url)
print(resp.text)
	