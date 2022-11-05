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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

