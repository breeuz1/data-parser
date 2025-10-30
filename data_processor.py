import pandas as pd


try:
    time = int(input("После скольки показать вам новости -- "))
    news = pd.read_json("data-parser/data/news.json")
    after_time = news[news["date"].dt.hour > time]

    after_time.to_csv("data-parser/data/news.csv", index=False)
    longest_title = news.loc[news["title"].str.len().idxmax()]
    shortest_title = news.loc[news["title"].str.len().idxmin()]
    print(
        f"Файл создан! Новостей после {time}:00 - {len(after_time)}\n #Всего новостей -- {len(news)}\n #Средняя длина заголовков -- {news['title'].str.len().mean()}\n #Самый длинный заголовок -- {longest_title['title']} | Длинна которого {len(longest_title['title'])}\n #Самый короткий заголовок -- {shortest_title['title']} | Длинна которого {len(shortest_title['title'])}"
    )
except FileNotFoundError:
    print("Файл news.json не найден! Сначала запусти парсер.")
