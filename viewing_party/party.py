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
    if not user_data or not movie:
        return user_data

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie) :
    if not user_data or not movie:
        return user_data

    user_data["watchlist"].append(movie)

    return user_data

def movie_title_in_list(movies,title):
    if not movies or not title:
        return None

    for movie in movies:
        if movie["title"] == title:
            return movie
    
    return None


#Moves movie from watchlist to watched for the given user
def watch_movie(user_data,title):
    if not user_data or not title:
        return user_data

    movie = movie_title_in_list(user_data["watchlist"],title)
    if movie:
        user_data["watched"].append(movie)
        user_data["watchlist"].remove(movie)

    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data) :
    avg = 0
    if not user_data:
        return avg

    watched = len (user_data["watched"])
    if watched == 0:
        return avg

    for movie in user_data["watched"]:
        avg += movie["rating"]

    return avg/watched

def get_most_watched_genre(user_data):
    fav_genre = None
    max_watched = 0
    if not user_data:
        return fav_genre

    genres = dict()
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genres.keys(): 
            genres[genre]=1
        else:
            genres[genre]+=1

        if genres[genre]>max_watched:
            max_watched = genres[genre]
            fav_genre = genre

    return fav_genre
            
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_not_watched_by_friends(watched, friends):
    if watched is None or friends is None:
        return None

    if friends==[]:
        return watched

    #created friends joined watched list
    friends_watched = list()
    for friend in friends:
        for movie in friend["watched"]:
            if movie not in friends_watched:
                friends_watched.append(movie)

    user_unique = list()
    for movie in watched:
        if movie not in friends_watched:
            user_unique.append(movie)

    return user_unique
    

def get_unique_watched(user_data):
    if not user_data:
        return None
    
    return  get_not_watched_by_friends(user_data["watched"],user_data["friends"])


def get_friends_unique_watched(user_data) :
    if not user_data:
        return None

    friends_unique = list()

    friends = user_data["friends"]
    for friend in friends:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique:
                friends_unique.append(movie)

    return friends_unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data) :
    if not user_data:
        return None

    recomendations = list()
    friends_watched = get_friends_unique_watched(user_data)

    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"] and movie not in recomendations:
            recomendations.append(movie)

    return recomendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    if not user_data:
        return None

    recomendations = list()
    friends_watched = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)

    for movie in friends_watched:
        if movie["genre"] == favorite_genre and movie not in recomendations:
            recomendations.append(movie)

    return recomendations

def get_rec_from_favorites(user_data):
    if not user_data:
        return None
    
    return get_not_watched_by_friends(user_data["favorites"],user_data["friends"])
