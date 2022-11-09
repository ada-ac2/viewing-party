# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
   if title == None or genre == None or rating == None:
       return None
   dict = {}
   dict["title"] = title
   dict["genre"] = genre
   dict["rating"] = rating
   return dict
    

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            add_to_watched(user_data, user_data["watchlist"][i])
            del user_data["watchlist"][i]
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

