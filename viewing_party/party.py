# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        return {   "title": title,
        "genre": genre,
        "rating": rating
        }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
            break    
    return user_data

    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0.0
    user_data_len = len(user_data["watched"])
    if user_data_len >0:
        for movie in user_data["watched"]:
            sum += movie["rating"]

        return sum/user_data_len
    else:
        return sum


def get_most_watched_genre(user_data):
    most_watched_dict = {}
    user_data_len = len(user_data["watched"])

    if user_data_len > 0:
        for movie in user_data["watched"]:
            if movie["genre"] in most_watched_dict:
                most_watched_dict[movie["genre"]] += 1
            else:
                most_watched_dict[movie["genre"]] = 0

        most_watched_genre = max(most_watched_dict, key=most_watched_dict.get)
        return most_watched_genre
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    friends_movies = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])

    for user_movie in user_data["watched"]:
        if user_movie["title"] not in friends_movies:
            unique_movies.append(user_movie)

    return unique_movies
        
def get_friends_unique_watched(user_data):
    unique_movies = []
    user_movies = []

    for user_movie in user_data["watched"]:
        user_movies.append(user_movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_movies and movie not in unique_movies:
                unique_movies.append(movie)

    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_recs = []
    friends_unique_data = get_friends_unique_watched(user_data)

    if len(friends_unique_data) >0 and len(user_data["watched"])> 0:
        for movie in friends_unique_data:
            if movie["host"] in user_data["subscriptions"]:
                friends_recs.append(movie)

    return friends_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    rec_by_genre = []
    most_watched_genre = get_most_watched_genre(user_data)
    recs = get_available_recs(user_data)
    for movie in recs:
        if movie["genre"] == most_watched_genre:
            rec_by_genre.append(movie)

    return rec_by_genre

def get_rec_from_favorites(user_data):
    rec_from_favorites = []
    unique_watched = get_unique_watched(user_data)

    if len(user_data["favorites"]) >0:
        for movie in unique_watched:
            if movie in user_data["favorites"]:
                rec_from_favorites.append(movie)           
    return rec_from_favorites
