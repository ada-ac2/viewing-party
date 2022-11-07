# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not bool(title) or not bool(genre) or not bool(rating):
        return None
    
    new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    if not bool(movie):
        return user_data
    user_data["watched"].append(movie)
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

