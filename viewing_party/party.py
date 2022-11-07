from collections import Counter
import copy

# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    return movie_dict


def add_to_watched(user_data, movie):
    user_data.get("watched").append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data.get("watchlist").append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist_movies = user_data.get("watchlist")
    for i in range(len(watchlist_movies)):
        if watchlist_movies[i].get("title") == title:
            watched_movie = watchlist_movies.pop(i)
            user_data.get("watched").append(watched_movie['title'])
            break

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    sum_rating = 0
    total_movie = 0
    for records in user_data["watched"]:
        sum_rating += records["rating"]
        total_movie += 1

    return sum_rating / total_movie


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_list = []
    for record in user_data["watched"]:
        genre_list.append(record['genre'])

    genre_counter = Counter(genre_list)

    most_view_genre = max(genre_counter, key=genre_counter.get)
    return most_view_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    result = []
    friends_watched_movies = set()

    for friend in user_data["friends"]:
        for movie_record in friend["watched"]:
            friends_watched_movies.add(movie_record["title"])

    for movies_watched in user_data["watched"]:
        if movies_watched["title"] not in friends_watched_movies:
            result.append(movies_watched)
    return copy.deepcopy(result)


def get_friends_unique_watched(user_data):
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie_record in friend["watched"]:
            if movie_record not in friends_watched_movies:
                friends_watched_movies.append(movie_record)

    for movies_watched in user_data["watched"]:
        if movies_watched in friends_watched_movies:
            friends_watched_movies.remove(movies_watched)

    return copy.deepcopy(friends_watched_movies)


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    result = []
    friends_watched_movies = get_friends_unique_watched(user_data)

    for data in friends_watched_movies:
        if data["host"] in user_data["subscriptions"]:
            result.append(data)
    return copy.deepcopy(result)


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    result = []
    most_frequent_genre = get_most_watched_genre(user_data)
    qualified_movies = get_friends_unique_watched(user_data)

    for data in qualified_movies:
        if data["genre"] == most_frequent_genre:
            result.append(data)
    return copy.deepcopy(result)


def get_rec_from_favorites(user_data):
    result = []
    unique_user_movies = get_unique_watched(user_data)

    for data in user_data["favorites"]:
        if data in unique_user_movies:
            result.append(data)
    return copy.deepcopy(result)
