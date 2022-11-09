# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    movies = {}

    if movie_title == None or genre == None or rating == None :
        return None

    movies["title"] = movie_title
    movies["genre"] = genre
    movies["rating"] = rating

    return movies

# movie_title = "MOVIE_TITLE_1"
# genre = "GENRE_1"
# rating = "RATING_1"

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
# USER_DATA_2 = {
#     "watched": [
#         "FANTASY_1", 
#         "FANTASY_2", 
#         "FANTASY_3", 
#         "ACTION_1", 
#         "INTRIGUE_1", 
#         "INTRIGUE_2"
#         ],  
#     "friends": [
#         {
#             "watched": [
#                 "FANTASY_1",
#                 "FANTASY_3",
#                 "FANTASY_4",
#                 "HORROR_1",
#             ]
#         },
#         {
#             "watched": [
#                 "FANTASY_1",
#                 "ACTION_1",
#                 "INTRIGUE_1",
#                 "INTRIGUE_3",
#             ]
#         }
#     ]  
# }

# def get_unique_watched(user_data):
#     user_movies_set = set(user_data["watched"])
#     friends_movies_set = set()

#     for friend in user_data["friends"]:
#         # print(f"friend['watched'] converted to a set is{set(friend['watched'])}")
#         # print(f"friends_movies_set is {friends_movies_set}")
#         friends_movies_set.update(set(friend["watched"]))

#     unique_movies = user_movies_set.difference(friends_movies_set)
#     return unique_movies

# print(get_unique_watched(USER_DATA_2))

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


