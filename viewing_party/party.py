# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    # create a movie dictionary to store info of each movie
    if title is None or genre is None or rating is None:
        return None
    else:
        movie = dict()
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie


def add_to_watched(user_data, movie):
    watched = dict()
    watched["title"] = movie["title"]
    watched["genre"] = movie["genre"]
    watched["rating"] = movie["rating"]
    user_data["watched"].append(watched)
    return user_data


def add_to_watchlist(user_data, movie):
    watchlist = dict()
    watchlist["title"] = movie["title"]
    watchlist["genre"] = movie["genre"]
    watchlist["rating"] = movie["rating"]
    user_data["watchlist"].append(watchlist)
    return user_data


def watch_movie(user_data, title):
    for m in user_data["watchlist"]:
        if m["title"] == title:
            user_data["watchlist"].remove(m)
            user_data["watched"].append(title)
            break
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    result = 0
    count = len(user_data["watched"])
    for m in user_data["watched"]:
        result += m["rating"]
    if count:
        result /= count
    return result


def get_most_watched_genre(user_data):
    genre_dict = dict()
    result = None
    if user_data["watched"]:
        for m in user_data["watched"]:
            if m["genre"] in genre_dict.keys():
                genre_dict[m["genre"]] += 1
            else:
                genre_dict[m["genre"]] = 1
        # sort dictionary in ascending order
        result = sorted(genre_dict.items(), key=lambda x: x[1])[-1][0]
    return result


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = list()
    for f in user_data["friends"]:
        for m in f["watched"]:
            friends_watched.append(m)
    unique = [i for i in user_watched if i not in friends_watched]
    return unique


def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = list()
    for f in user_data["friends"]:
        for m in f["watched"]:
            friends_watched.append(m)
    # remove duplicates
    friends_watched_nd = list()
    [friends_watched_nd.append(i) for i in friends_watched if i not in friends_watched_nd]
    unique = [i for i in friends_watched_nd if i not in user_watched]
    return unique

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs = list()
    friends_watched = list()
    for f in user_data["friends"]:
        for m in f["watched"]:
            friends_watched.append(m)
    # remove duplicates
    friends_watched_nd = list()
    [friends_watched_nd.append(i) for i in friends_watched if i not in friends_watched_nd]

    if (len(user_data["subscriptions"])!=0) and (len(friends_watched)!=0):
        for i in friends_watched_nd:
            if i["host"] in user_data["subscriptions"] and i not in user_data["watched"]:
                recs.append(i)
    return recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    unwatched = get_friends_unique_watched(user_data)
    recs = list()
    for i in unwatched:
        if i["genre"] == genre:
            recs.append(i)
    return recs

def get_rec_from_favorites(user_data):
    friends_watched = list()
    for f in user_data["friends"]:
        for m in f["watched"]:
            if m not in friends_watched:
                friends_watched.append(m)
    watched = get_unique_watched(user_data)
    recs = list()
    for i in user_data["favorites"]:
        if i not in friends_watched or i in watched:
            recs.append(i)
    return recs
