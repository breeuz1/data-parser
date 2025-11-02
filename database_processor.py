import sqlite3
import json

try:
    con = sqlite3.connect("data-parser/data/database.db")
    cursor = con.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS News (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    author TEXT NOT NULL,
    date TEXT NOT NULL
    )
    """
    )

    with open("data-parser/data/news.json", "r", encoding="utf-8") as f:
        news_data = json.load(f)
    print(f"Прочитано {len(news_data)} новостей из JSON")

    for news in news_data:
        title = news["title"]
        url = news["url"]
        author = news["author"]
        date = news["date"]

        cursor.execute(
            "INSERT INTO News (title, url, author, date) VALUES (?, ?, ?, ?)",
            (title, url, author, date),
        )

    con.commit()

    cursor.execute("SELECT * FROM News")
    all_news = cursor.fetchall()
    for news in all_news:
        print(*news)

    author = input("Какого автора хотите почитать: ")
    if author in [news["author"] for news in news_data]:
        cursor.execute("SELECT * FROM News WHERE author= ?", (author,))
        author_news = cursor.fetchall()
        for news in author_news:
            print(*news)
    else:
        print("Такого автора нет!")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    if con:
        con.close()
