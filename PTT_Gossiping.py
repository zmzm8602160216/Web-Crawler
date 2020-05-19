import  requests
import  json

URL = "https://www.ptt.cc/bbs/Gossiping/index.html"
# 設定Header與Cookie
my_headers = {'cookie': 'over18=1;'}

response = requests.get(URL, headers = my_headers)
print(response.text)
