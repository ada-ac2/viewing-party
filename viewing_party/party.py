# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title == None or genre == None or rating == None:
        return None
    else:
    
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }

        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):

    for movie_entry in user_data["watchlist"]:
        if movie_entry["title"] == movie:
            user_data["watched"].append(movie_entry)
            user_data["watchlist"].remove(movie_entry)
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) != 0:
        sum = 0
        for movie in user_data["watched"]:
            sum += movie["rating"]
        return sum / len(user_data["watched"])
    else:
        return 0

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) != 0:
        genres = {}

        for movie_entry in user_data["watched"]:
            if movie_entry["genre"] not in genres:
                genres[movie_entry["genre"]] = 1
            else:
                genres[movie_entry["genre"]] += 1
        
        return max(genres, key=genres.get)
    else:
        return None

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

