# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not bool(title) or not bool(genre) or not bool(rating):
        return None

    new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie


def add_to_watched(user_data, movie):
    if not bool(movie):
        return user_data
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    if not bool(movie):
        return user_data
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data

# movie not in watchlist
# move in watchlist move to watched
# check watchlist[title] for matches with title
# list user_data[tc]
# what if it already exists in watched_movie

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

