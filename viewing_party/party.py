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
    if user_data is None:
        return None

    if movie is None:
        return user_data

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie) :
    if user_data is None:
        return None

    if movie is None:
        return user_data

    user_data["watchlist"].append(movie)

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

