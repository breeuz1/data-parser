import requests


url = "https://newsapi.org/v2/top-headlines"
category = input(
    "Choose one category and write here(Categories: business; entertainment; general; health; science; sports; technology): "
)
response = requests.get(f"{url}?category={category}&apiKey=api_key")
json_response = response.json()
count_news = 1
for news in json_response["articles"]:
    print(
        f"Articles {count_news}",
        news["author"],
        news["title"],
        news["description"],
        news["publishedAt"],
        sep="\n",
    )
    count_news += 1
    print()
