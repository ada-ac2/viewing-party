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
    if user_data is None or movie is None:
        return user_data

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie) :
    if user_data is None or movie is None:
        return user_data

    if movie is None:
        return user_data

    user_data["watchlist"].append(movie)

    return user_data

def movie_title_in_list(movies,title):
    if movies is None or title is None:
        return None

    for movie in movies:
        if movie["title"] == title:
            return movie
    
    return None


#Removes movie from watchlist to watched for the given user
def watch_movie(user_data,title):
    if user_data is None or title is None:
        return user_data

    movie = movie_title_in_list(user_data["watchlist"],title)
    if movie:
        user_data["watched"].append(movie)
        user_data["watchlist"].remove(movie)

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

