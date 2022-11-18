# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movie = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie = {"title" : title, "genre" : genre, "rating" : rating}
        return movie

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = 0
    rating_avg = 0.0

    if len(user_data["watched"]) == 0:
        return rating_avg
    else:
        for movie in user_data["watched"]:
            rating_total += movie["rating"]
    rating_avg = rating_total/len(user_data["watched"])

    return rating_avg

def get_most_watched_genre(user_data):
    genre_count = {}
    genre_temp = ""
    count_temp = 0
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_count.keys():
                genre_count[movie["genre"]] = 1
            else:
                genre_count[movie["genre"]] += 1

    for genre,count in genre_count.items():
        if count > count_temp:
            count_temp = count
            genre_temp = genre

    return genre_temp

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

#return list of movie that friends watched
def friends_watched_movie(user_data):
    friend_watched_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_movie.append(movie)
    return friend_watched_movie

def get_unique_watched(user_data):
    unique_watch = []
    friends_list = friends_watched_movie(user_data)
    for movie in user_data["watched"]:
        if movie not in friends_list:
            unique_watch.append(movie)

    return unique_watch

#Return movies at least one of the user's friends have watched, but the user has not watched.
def get_friends_unique_watched(user_data):
    friend_unique_watched = []
    friends_list = friends_watched_movie(user_data)
    for movie in friends_list:
        if (movie not in user_data["watched"] and movie not in friend_unique_watched):
            friend_unique_watched.append(movie)
    return friend_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
#Return the list of recommended movies
def get_available_recs(user_data):
    recs_movie = []
    friend_unique_movie = get_friends_unique_watched(user_data)
    for i in range(len(friend_unique_movie)):
        if friend_unique_movie[i]["host"] in user_data["subscriptions"]:
            recs_movie.append(friend_unique_movie[i])

    return recs_movie


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#return a list of recomended movies with user's most watched genre
def get_new_rec_by_genre(user_data):
    recs_movie = []
    most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_movie = get_friends_unique_watched(user_data)
    for i in range(len(friend_unique_movie)):
        if friend_unique_movie[i]["genre"] == most_watched_genre:
            recs_movie.append(friend_unique_movie[i])
    return recs_movie

#return a list of recomended movies none of friends watched
def get_rec_from_favorites(user_data):
    recs_movie = []
    user_unique_watched = get_unique_watched(user_data)
    for i in range(len(user_unique_movie)):
        if friend_unique_movie[i] in user_data["favorites"]:
            recs_movie.append(user_unique_movie[i])
    return recs_movie
