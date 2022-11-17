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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

