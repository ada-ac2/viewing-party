# ------------- WAVE 1 --------------------
movie = {}
watched_movie_lst = []
watch_lst = []
def create_movie(title, genre, rating):
    if  title and genre and rating :
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    elif title or genre or rating == False:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"] = watched_movie_lst
    watched_movie_lst.append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = watch_lst
    watch_lst.append(movie)
    return user_data 

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            movie_change = user_data["watchlist"][i]
            user_data["watchlist"].pop(i)
            user_data["watched"].append(movie_change)
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

