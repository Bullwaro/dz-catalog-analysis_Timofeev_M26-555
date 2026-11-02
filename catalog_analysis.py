import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

#1 Средний рейтинг всех фильмов
def average_rating(movies: list[dict]):
    avg_rating = 0

    for movie in movies:
        avg_rating += movie["rating"]
        
    return round(avg_rating / len(movies), 1)

#1 Самый старый фильм в годах, самый новый фильм в годах, среднее
def catalog_age_stats(movies: list[dict], current_year=2026):
    oldest = float("inf")
    youngest = float("-inf")
    avg_year = 0

    for movie in movies:
        oldest = movie["year"] if movie["year"] < oldest else oldest
        youngest = movie["year"] if movie["year"] > youngest else youngest
        avg_year += movie["year"]
    avg_year /= len(movies)

    return oldest, youngest, math.ceil(avg_year)

#1 Перевод продолжительности в часы и минуты
def duration_in_hours(minutes):
    hours = minutes // 60
    minutes %= 60
    return hours, minutes

#2 Субъективная оценка фильма по рейтингу
def rating_tier(rating):
    if 7 <= rating < 9:
        return 'хорошо'
    elif 5 <= rating < 7:
        return 'средне'
    else:
        return 'шедевр' if rating >= 9 else 'слабо'

#2 Субъективная оценка фильма по дате выхода
def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _ if year < 2015:
            return 'старые'

#3 Количество фильмов длиннее threshold
def count_long_movies(movies: list[dict], threshold = 120):
    long_movies_counter = 0

    for movie in movies:
        if movie['duration_min'] > threshold:
            long_movies_counter += 1
    return long_movies_counter


#3 Вывод некомедийных фильмов
for movie in movies:
    if 'comedy' in movie['genres']:
        continue
    print(movie['title'])

#3 Поиск первого шедевра
i = 0
masterpiece = ''
while i < len(movies):
    if movies[i]['rating'] > 9:
        masterpiece = movies[i]['title']
        break
    i += 1
else:
    print('Шедевров не найдено')



print(average_rating(movies))
print(catalog_age_stats(movies))
print(duration_in_hours(movies[0]["duration_min"]))
print(rating_tier(5))
print(decade_label(2016))
print(count_long_movies(movies))