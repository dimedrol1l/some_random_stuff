import pandas as pd

movies = pd.read_csv('/Users/mihailsavic/Downloads/ml-latest-small/movies.csv')
ratings = pd.read_csv('/Users/mihailsavic/Downloads/ml-latest-small/ratings.csv')

ratings_5 = ratings[ratings['rating'] == 5.0]
count = ratings_5['movieId'].value_counts().reset_index()
count.columns = ['movieId', 'count']
count = count.merge(movies, on='movieId')
most_rated = count.loc[count['count'].idxmax()]
print(f"Фильм с наибольшим количеством оценок 5.0: {most_rated['title']} ({most_rated['count']} оценок)")


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fortrader.org/quotes/ruble"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table")

if table:
    headers = [header.text.strip() for header in table.find_all("th")]
    rows = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        rows.append([cell.text.strip() for cell in cells])
    df = pd.DataFrame(rows, columns=headers)
    df.columns = df.columns.str.replace('\t', '')
    df = df.applymap(lambda x: x.replace('\t', '') if isinstance(x, str) else x)
    print(df)
else:
    print("Таблица не найдена на странице")

import pandas as pd

def classify_movies(ratings_csv, movies_csv, output_csv):
    movies = pd.read_csv('/Users/mihailsavic/Downloads/ml-latest-small/movies.csv')
    ratings = pd.read_csv('/Users/mihailsavic/Downloads/ml-latest-small/ratings.csv')

    def classify_rating(rating):
        if rating <= 2:
            return 'низкий рейтинг'
        elif rating <= 4:
            return 'средний рейтинг'
        elif rating >= 4.5:
            return 'высокий рейтинг'

    ratings['class'] = ratings['rating'].apply(classify_rating)

    ratings.to_csv(output_csv, index=False)

    print(f"Классификация завершена. Результат сохранен в {output_csv}")

classify_movies('ratings.csv', 'movies.csv', 'classified_ratings.csv')



