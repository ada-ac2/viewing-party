# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = dict()
    if title == None or genre == None or rating == None:
        return None
    else: 
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for data in user_data["watchlist"]:
        if title == data["title"]:
            user_data["watched"].append(data)
            #index = user_data["watchlist"].index(data)
            #user_data["watchlist"].pop(index)
            user_data["watchlist"].remove(data)
            return user_data
        
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    average_rating = 0.0
    rating = 0.0

    if len(user_data["watched"]) == 0:
        return average_rating

    for movie in user_data["watched"]:
        rating += movie["rating"]
    average_rating = rating / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_frequently = dict()
    max = 0
    most_watched_genre = ""
    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequently:
            genre_frequently[movie["genre"]] += 1
        else:
            genre_frequently[movie["genre"]] = 1
        
        if max < genre_frequently[movie["genre"]]:
            max = genre_frequently[movie["genre"]]
            most_watched_genre = movie["genre"]
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

def get_unique_watched(user_data):
    user_set = user_watched(user_data)
    friend_set = friends_watched(user_data)
    unique_title = user_set.difference(friend_set)
    unique_watched = list()

    for title in unique_title:
        for movie in user_data["watched"]:
            if title == movie["title"]:
                unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    user_set = user_watched(user_data)
    friends_set = friends_watched(user_data)

    unique_title = friends_set.difference(user_set)
    user_has_not_watched = list()
        
    for title in unique_title:
        for movie in user_data["friends"]:
            for watched in movie["watched"]:
                if title == watched["title"] and watched not in user_has_not_watched:
                    user_has_not_watched.append(watched)
    return user_has_not_watched
            

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

