import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
for start_num in range(0,250,25):
    respense = requests.get(f"https://movie.douban.com/top250?start={start_num}&filter=", headers=headers)
    html = respense.text
    soup = BeautifulSoup(html, "html.parser")
    all_title = soup.findAll("span", attrs={"class": "title"})
    for title in all_title:
        title_string = title.string
        if "/" not in title_string:
            with open("C:/Users/32573/Desktop/doubantop250.txt", "a", encoding="utf-8") as f:
                f.write(title_string+"\n")
