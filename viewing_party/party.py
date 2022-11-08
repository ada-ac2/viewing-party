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
    watched_movie = {}
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
                #the movie_title is present in watchlist
                watched_movie = movie
                user_data["watchlist"].remove(watched_movie)
                add_to_watched(user_data, watched_movie)
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

