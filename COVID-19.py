# 套件
import requests
import json


response = requests.get("https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json")

#讀取Json格式
jd = json.loads(response.text)
print(jd[0])