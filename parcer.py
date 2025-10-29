import requests
from bs4 import BeautifulSoup
import json

url = "https://habr.com/ru/articles"

response = requests.get(url)

allNews = []

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article")

new_list = []
for article in articles:
    title = article.find("h2").text.strip()
    link = article.find("a")["href"]
    author = article.find("a")["title"]
    date = article.find("time")["title"]

    if link.startswith("/"):
        link = "https://habr.com" + link

    new_list.append(
        {
            "title": title,
            "url": link,
            "author": author,
            "date": date,
        }
    )


with open("news.json", "w", encoding="utf-8") as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)

print(f"Спаршено {len(new_list)} новостей!")
