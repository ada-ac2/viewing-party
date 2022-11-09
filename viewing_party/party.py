# ------------- WAVE 1 --------------------

# returns a dict 
def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None
# add and returns the movie to "watched" list inside of userdata
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# add and returns movie to "watchlist" list inside of user_data
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# If title is a movie in user's watchlist it will remove it from watchlist and add it to watched list
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            print(movie)
    i = 0
    while i < len(user_data["watchlist"]):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watchlist"].pop(i)
            print(user_data["watchlist"])
        i += 1
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

