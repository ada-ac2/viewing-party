import statistics
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
    :params: dict - user_data: "watched" movies
             dict - movie: movie details
    :returns: nested dict - updated_data: updated watched movies 
    """
    # copy user_data
    updated_data = user_data.copy()
    # update watched movie
    updated_data["watched"] = [movie]
    return updated_data


def add_to_watchlist(user_data, movie):
    """
    Updates dataset to include movies to be watched and details
    :params: dict - user_data: "watchlist" movies
             dict - movie: movie details
    :returns: nested dict - updated_data: updated watchlist movies
    """
    # copy user data
    updated_data = user_data.copy()
    # update watchlist movie
    updated_data["watchlist"] = [movie]
    return updated_data

def watch_movie(janes_data, MOVIE_TITLE_1):
    """
    Moves a movie from watchlist to watched
    :params: dict - janes_data: dataset containing watched and watchlist movies
             str - MOVIE_TITLE_1: movie title
    :returns: nested dict - updated_data: updated watched/watchlist movies
    """
    # copy user data
    updated_data = janes_data.copy()
    # iterate through watchlist movies
    for movie in updated_data['watchlist']:
        # assume movie title == MOVIE_TITLE_1
        if movie['title'] == MOVIE_TITLE_1:
            # remove from watchlist
            updated_data['watchlist'].remove(movie)
            # add to watched
            updated_data['watched'].append(movie)
    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(janes_data):
    """
    Calculates movie rating average in watched movies
    :params: dict - janes_data: dataset containing watched and watchlist movies
    :returns: float - average: movie rating average
    """
    # collect ratings of movies watched
    ratings = []
    for movie in janes_data['watched']:
        ratings.append(movie['rating'])
    if len(ratings) == 0:
        return 0
    # calculate the average
    average = sum(ratings)/len(ratings)
    return average

    
def get_most_watched_genre(janes_data):
    """
    Collects watched movie genres and generates most popular genre by calculating the mode.
    :params: dict - janes_data: dataset containing watched and watchlist movies
    :returns: str - popular_genre: most popular movie genre watched
    """
    # collect genres of movies watched
    genres = []
    for movie in janes_data['watched']:
        genres.append(movie['genre'])
    if len(genres) == 0:
        return None
    # collect highest frequency movie genre
    popular_genre = statistics.mode(genres)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(amandas_data):
    """
    Compares amandas watched movies to friends watched movies to return list of amandas unique watched movies
    :params: dict - amandas_data: dataset containing amandas and friends watched movies
    :returns: list - amandas_unique_movies: list of movies only amanda watched
    """
    # iterate through amandas watched movies
    amandas_movies = []
    for movie in amandas_data['watched']:
        amandas_movies.append(movie)
    # iterate through friends watched movies
    friends_movies = []
    for movies in amandas_data['friends']:
        for movie in movies['watched']:
            friends_movies.append(movie)
    # collect diff between amandas and friends
    amandas_unique_movies = []
    for movie in amandas_movies:
        if movie not in friends_movies:
            amandas_unique_movies.append(movie)
    return amandas_unique_movies


def get_friends_unique_watched(amandas_data):
    """
    Compares amandas watched movies to friends watched movies to return list of friends unique watched movies
    :params: dict - amandas_data: dataset containing amandas and friends watched movies
    :returns: list - friends_unique_movies: list of movies only friends watched
    """
    # iterate through amandas watched movies
    amandas_movies = []
    for movie in amandas_data['watched']:
        amandas_movies.append(movie)
    # iterate through friends watched movies
    friends_movies = []
    for movies in amandas_data['friends']:
        for movie in movies['watched']:
            # assume movie not already in friends_movies
            if movie not in friends_movies:
                # add to friends_movies
                friends_movies.append(movie)
    # collect diff between amandas and friends
    friends_unique_movies = []
    for movie in friends_movies:
        if movie not in amandas_movies:
            friends_unique_movies.append(movie)
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

