import requests
response = requests.get("https://baike.baidu.com/item/%E6%B5%B7%E7%87%95/2611734?fr=aladdin/")
if response.ok:
    print(response.text)
else:
    print("请求失败")