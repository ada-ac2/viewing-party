# ------------- WAVE 1 --------------------

def create_movie(title=None, genre=None, rating=None):
    """
    Creates a dictionary with movie details
    :params: str: title - movie title; default=None
             str: genre - movie genre; default=None
             str: rating - movie rating; default=None
    :returns: new_movie - dictionary
    """
    dets = [title, genre, rating]
    # create dictionary with movie details
    new_movie = {}
    keys = ["title", "genre", "rating"]
    for key, det in zip(keys, dets):
        new_movie[key] = det
    # handle missing movie details
    if any(x == None for x in dets):
        new_movie = None
    return new_movie


def add_to_watched(user_data, movie):
    """
    Updates dataset to include watched movies and details
    :params: dict: user_data - "watched" movies
             dict: movie - movie details
    :returns: nested dict - "watched" movie with details
    """
    updated_data = user_data.copy()
    updated_data["watched"] = [movie]
    return updated_data


def add_to_watchlist(user_data, movie):
    """
    Updates dataset to include movies to be watched and details
    :params: dict: user_data - "watchlist" movies
             dict: movie - movie details
    :returns: nested dict - "watchlist" movie with details
    """
    updated_data = user_data.copy()
    updated_data["watchlist"] = [movie]
    return updated_data

def watch_movie(janes_data, MOVIE_TITLE_1):
    updated_data = janes_data.copy()
    for movie in updated_data['watchlist']:
        if movie['title'] == MOVIE_TITLE_1:
            updated_data['watchlist'].remove(movie)
            updated_data['watched'].append(movie)
    return updated_data

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

