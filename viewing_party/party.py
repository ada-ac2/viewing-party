# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    return {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    count, total_rating = 0, 0.0
    for movie in user_data["watched"]:
        count += 1
        total_rating += movie["rating"]
    return total_rating / count if count != 0 else 0.0

def get_most_watched_genre(user_data):
    genres = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1
    sorted_genres = sorted(genres.items(), key=lambda x:x[1], reverse=True)
    return sorted_genres[0][0] if len(sorted_genres) > 0 else None


        



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

