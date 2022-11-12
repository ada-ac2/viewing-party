# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if not title or not genre or not rating:
        return None
    movie = dict() 
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for data in user_data["watchlist"]:
        if title == data["title"]:
            user_data["watched"].append(data)
            user_data["watchlist"].remove(data)
            return user_data
        
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0

    average_rating = 0.0
    sum_rating = 0.0
    sum_rating = sum(movie["rating"] for movie in user_data["watched"])
    average_rating = sum_rating / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_frequently = dict()
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        if movie["genre"] in genre_frequently:
            genre_frequently[movie_genre] += 1
        else:
            genre_frequently[movie_genre] = 1
       
    most_watched_genre = max(genre_frequently, key=genre_frequently.get)
    return most_watched_genre        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def user_watched(user_data):
    user_set = set()
    for movie in user_data["watched"]:
        user_set.add(movie["title"])
    return user_set

def friends_watched(user_data):
    friend_set = set()
    for watched in user_data["friends"]:
        for movie in watched["watched"]:
            friend_set.add(movie["title"])
    return friend_set

def get_difference(x, y):
    return x.difference(y)

def get_unique_watched(user_data):
    user_set = user_watched(user_data)
    friend_set = friends_watched(user_data)
    unique_title = get_difference(user_set, friend_set)
    unique_watched = list()

    for movie in user_data["watched"]:
        if movie["title"] in unique_title:
            unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    user_set = user_watched(user_data)
    friends_set = friends_watched(user_data)

    unique_title = get_difference(friends_set, user_set)
    user_has_not_watched = list()
        
    for movie in user_data["friends"]:
        for watched in movie["watched"]:
            if watched["title"] in unique_title and watched not in user_has_not_watched:
                    user_has_not_watched.append(watched)
    return user_has_not_watched
                   
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_has_not_watched = get_friends_unique_watched(user_data)
    recommended_movies = [movie for movie in user_has_not_watched
                          if movie["host"] in user_data["subscriptions"]]

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_genre = get_most_watched_genre(user_data)
    user_has_not_watched = get_friends_unique_watched(user_data)
    recommended_movies = [movie for movie in user_has_not_watched
                          if movie["genre"] == most_genre]
    return recommended_movies

def get_rec_from_favorites(user_data):
    friends_have_not_watched = get_unique_watched(user_data)
    recommended_movies = [user_movie for user_movie in user_data["favorites"]
                          if user_movie in friends_have_not_watched]
    
    return recommended_movies