# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    movies = {}

    if movie_title == None or genre == None or rating == None :
        return None

    movies["title"] = movie_title
    movies["genre"] = genre
    movies["rating"] = rating

    return movies


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie_title in movie.values():
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def  get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0

    ratings_sum = 0
    movies_num = 0
    
    for movie in user_data["watched"]:
        movies_num += 1
        ratings_sum += movie["rating"]

    average_rating = ratings_sum/movies_num

    return average_rating


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    
    genre_frequency = {}

    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequency:
            genre_frequency[movie["genre"]] += 1
        else:
            genre_frequency[movie["genre"]] = 1

    max_num_for_genre = max(genre_frequency.values())

    for genre, frequency in genre_frequency.items():
        if frequency == max_num_for_genre:
            return genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_collective_friends_movies(user_data):
    friends_movies_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies_list:
                friends_movies_list.append(movie)

    return friends_movies_list


def get_unique_watched(user_data):
    unique_movies = []
    friends_movies_list = get_collective_friends_movies(user_data)

    for movie in user_data["watched"]:
        if movie not in friends_movies_list:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):
    unique_movies = []
    friends_movies_list = get_collective_friends_movies(user_data)

    for movie in friends_movies_list:
        if movie not in user_data["watched"]:
            unique_movies.append(movie)

    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    available_recommendations = []

    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            available_recommendations.append(movie)

    return available_recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommendation = []

    for movie in friends_unique_movies:
        if movie["genre"] == most_watched_genre:
            recommendation.append(movie)

    return recommendation


def get_rec_from_favorites(user_data):
    friends_movies_list = get_collective_friends_movies(user_data)
    recommendations = []

    for movie in user_data["favorites"]:
        if movie not in friends_movies_list:
            recommendations.append(movie)

    return recommendations


