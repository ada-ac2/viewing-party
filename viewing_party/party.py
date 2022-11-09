# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    movies = {}

    if movie_title == None or genre == None or rating == None :
        return None

    movies["title"] = movie_title
    movies["genre"] = genre
    movies["rating"] = rating

    return movies

movie_title = "MOVIE_TITLE_1"
genre = "GENRE_1"
rating = "RATING_1"

# print(create_movie(movie_title, genre, rating))

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# movie = {
#     "title": "MOVIE_TITLE_1",
#     "genre": "GENRE_1",
#     "rating": "RATING_1"
# }
# user_data = {
#     "watched": []
# }

# print(add_to_watched(user_data, movie))

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
# INTRIGUE_3 = {
#     "title": "Zero Dark Python",
#     "genre": "Intrigue",
#     "rating": 3.0
# }
# USER_DATA_2 = {
#     "watched": [
#         FANTASY_1, 
#         FANTASY_2, 
#         FANTASY_3, 
#         ACTION_1, 
#         INTRIGUE_1, 
#         INTRIGUE_2
#         ],    
# }

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



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

