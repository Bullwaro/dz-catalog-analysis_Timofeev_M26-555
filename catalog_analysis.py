import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, 
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, 
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, 
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, 
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, 
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, 
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, 
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, 
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, 
     "actors": ["P. Diaz", "T. Chalamet"]},
]

#1 Средний рейтинг всех фильмов
def average_rating(movies: list[dict]):
    avg_rating = 0

    for movie in movies:
        avg_rating += movie["rating"]
        
    return round(avg_rating / len(movies), 1)

#1 Самый старый фильм в годах, самый новый фильм в годах, среднее
def catalog_age_stats(movies: list[dict], current_year=2026):
    oldest = float("-inf")
    youngest = float("inf")
    avg_year = 0

    for movie in movies:
        age = current_year - movie['year']

        oldest = max(age, oldest)
        youngest = min(age, youngest)
        avg_year += age
    avg_year = avg_year / len(movies)

    return oldest, youngest, math.ceil(avg_year)

#1 Перевод продолжительности в часы и минуты
def duration_in_hours(minutes):
    hours = minutes // 60
    minutes %= 60
    return f"{hours}ч {minutes}м"

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
def count_long_movies(movies: list[dict], threshold=120):
    long_movies_counter = 0

    for movie in movies:
        if movie['duration_min'] > threshold:
            long_movies_counter += 1
    return long_movies_counter

#3 Вывод некомедийных фильмов
def noncomedy_films(movies: list[dict]):
    for movie in movies:
        if 'comedy' in movie['genres']:
            continue
        print(movie['title'])

#3 Поиск первого шедевра
def find_shedevr(movies: list[dict]):
    i = 0
    masterpiece = ''
    while i < len(movies):
        if movies[i]['rating'] > 9:
            masterpiece = movies[i]['title']
            break
        i += 1
    else:
        print('Шедевров не найдено')
    return masterpiece

#4 Привод строки к формату Title Case
def normalize_title(title: str):
    string_splitted = title.split()

    for i, word in enumerate(string_splitted):
        string_splitted[i] = word[0].upper() + word[1:]

    return ' '.join(string_splitted)

#4 Привод нормализованного название в "слаг"
def make_slug(title: str):
    return title.lower().replace(' ', '-')

#4 Информация о фильме
def format_report_line(movie: dict):
    return (f'"{normalize_title(movie['title'])}" '
            f'({movie['year']}) - '
            f'{movie['rating']}/10, '
            f'{duration_in_hours(movie['duration_min'])}, '
            f'жанры: {', '.join(sorted(movie['genres']))}')

#5 Список названий фильмов по убыванию рейтинга
def titles_sorted_by_rating(movies: list[dict]):
    sorted_movies = sorted(movies, key=lambda movie: movie['rating'], reverse=True)
    sorted_movies = [movie['title'] for movie in sorted_movies]

    return sorted_movies

#5 Топ-n фильмов по рейтингу
def top_n_by_rating(movies: list[dict], n=3):
    sorted_movies = sorted(
        movies, 
        key=lambda movie: movie['rating'], 
        reverse=True
    )[:n]
    top_titles = [(movie['title'], movie['rating']) for movie in sorted_movies]

    return top_titles

#6 Словарь-счётчик фильмов по жанрам
def count_by_genre(movies: list[dict]):
    genres_counter = {}

    for movie in movies:
        for genre in movie['genres']:
            genres_counter[genre] = genres_counter.get(genre, 0) + 1

    genres_counter = dict(
        sorted(
        genres_counter.items(), 
        key=lambda item: item[1], 
        reverse=True
        )
    )
    return genres_counter

#6 Словарь фильмов по актёрам
def actor_filmography(movies: list[dict]):
    actors_in_films = {}

    for movie in movies:
        for actor in movie['actors']:
            actors_in_films[actor] = actors_in_films.get(actor, [])
            actors_in_films[actor].append(movie['title'])

    return actors_in_films

#6 Словарь из фильмов с оценкой выше среднего при помощи генератора
films_better_avg = {
    movie['title']: movie['rating'] 
    for movie in movies 
    if movie['rating'] > average_rating(movies)}

#7 Множество всех уникальных жанров каталога
def all_genres(movies: list[dict]):
    genres = set()

    for movie in movies:
        genres |= movie['genres']

    return genres

#7 Множество актёров, снимавшихся в обоих фильмах
def common_actors(movie1: dict, movie2: dict):
    return set(movie1['actors']) & set(movie2['actors'])

#7 Уникальные жанры, встречающиеся в movies_a, но не в movies_b
def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]):
    genres_a = set()
    genres_b = set()

    for movie in movies_a:
        genres_a.update(movie['genres'])

    for movie in movies_b:
        genres_b.update(movie['genres'])

    return genres_a - genres_b

#8 Функция-генератор
def iter_high_rated(movies: list[dict], min_rating=8.0):
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie

#8 Вывод функции-генератора
for movie in iter_high_rated(movies):    
    print(format_report_line(movie))

#8 Генераторное выражение суммарной длительность фильмов с рейтингом выше 7 в минутах
def good_films_durability(movies: list[dict]):
    films_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)

#9 Итоговый отчёт
def build_report(movies):
    print('\nОТЧЁТ ПО КАТАЛОГУ')
    print('Средний рейтинг всего каталога: ', average_rating(movies)) #1
    print('Средний возраст фильмов:', catalog_age_stats(movies)[2], 'лет')
    print('Фильмов дольше двух часов: ', count_long_movies(movies)) #3
    print('\nТОП-3 фильма каталога по рейтингу зрителей:') #2, 4 и 5
    for title_rating in top_n_by_rating(movies, 3):
        for movie in movies:
            if title_rating[0] == movie['title']:
                print(format_report_line(movie))
    print('\nКоличество фильмов по жанрам:')
    genres_counter = count_by_genre(movies)
    for genre in genres_counter:
        print(f"{genre}: {genres_counter.get(genre)}")
    print('Все жанры каталога:', ', '.join(sorted(all_genres(movies))))

if __name__ == "__main__":
    build_report(movies)