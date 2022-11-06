# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if bool(title) and bool(genre) and bool(rating):
        return {
                    "title": title,
                    "genre": genre,
                    "rating":rating
               }
    else:
        None

def add_to_watched(user_data, movie):
    #user_data = {"watched": []}
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data = {"watchlist":[] }
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # user_data = {
    #                 "watchlist": [],
    #                 "watched": []
    #             }
    for m_to_watch in user_data["watchlist"]:
        title_to_watch = m_to_watch["title"]
        if title_to_watch == title:
            user_data["watchlist"].remove(m_to_watch)
            user_data["watched"].append(m_to_watch)
            return user_data
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

