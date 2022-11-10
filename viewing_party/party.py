# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data.setdefault("watched", []).append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data.setdefault("watchlist", []).append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie) 
            user_data["watchlist"].remove(movie)
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating_score = 0
    num_of_movies = len(user_data["watched"])
    for movie in user_data["watched"]:
        total_rating_score += movie["rating"]
    if num_of_movies == 0:
        return 0.0
    else:
        return total_rating_score / num_of_movies


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

