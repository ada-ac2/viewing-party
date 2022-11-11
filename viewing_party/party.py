# ------------- WAVE 1 --------------------

from shutil import move


def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data.setdefault("watched", []).append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data.setdefault("watchlist", []).append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie) 
            user_data["watchlist"].remove(movie)
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating_score = 0
    num_of_movies = len(user_data["watched"])
    for movie in user_data["watched"]:
        total_rating_score += movie["rating"]
    if num_of_movies == 0:
        return 0.0
    else:
        return total_rating_score / num_of_movies

def get_most_watched_genre(user_data):
    genres = {}
    if user_data["watched"] == []:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] in genres:
            genres[movie["genre"]] += 1
        else:
            genres[movie["genre"]] = 1
    #review this concept
    return max(genres, key=genres.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movies = []
    unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = []
    # user_movies = []
    # for movie in user_data["watched"]:
    #     user_movies.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_movies:
                friends_movies.append(movie)
    return friends_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"] and movie not in recommended_movies:
                recommended_movies.append(movie)
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    recommended_movies = get_available_recs(user_data)
    for movie in recommended_movies:
        if movie["genre"] not in fav_genre:
            recommended_movies.remove(movie)
    return recommended_movies

# def get_new_rec_by_genre(user_data):
#     fav_genre = get_most_watched_genre(user_data)
#     recommended_movies = []
#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             if movie not in user_data["watched"] and movie not in recommended_movies:
#                 recommended_movies.append(movie)
#     for movie in recommended_movies:
#         if movie["genre"] not in fav_genre:
#             recommended_movies.remove(movie)
#     return recommended_movies