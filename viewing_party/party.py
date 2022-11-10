# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    print(user_data)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    print(user_data)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
                #the movie_title is present in watchlist
                user_data["watchlist"].remove(movie)
                add_to_watched(user_data, movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if(len(user_data["watched"]) == 0):
        return 0
    sum = 0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    if (len(user_data["watched"]) == 0):
        return None
    most_watched = ""
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    most_watched = max(set(genre_list), key = genre_list.count)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched = []
    unique_watched = []
    for friends in user_data["friends"]:
        for watched in friends["watched"]:
            friends_watched.append(watched)
    
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_watched = []
    friends_unique_watched = []
    for friends in user_data["friends"]:
        for watched in friends["watched"]:
            friends_watched.append(watched)
    
    for movie in friends_watched:
        if movie not in user_data["watched"]:
            friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

