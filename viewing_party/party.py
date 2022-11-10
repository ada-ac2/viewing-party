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
def get_watched_avg_rating(user_data):
    #user_data = {"watched": []}
    total_rating == 0
    count = 0
    for watched_movie in user_data["watched"]:
        count += 1
        total_rating += watched_movie["rating"]
    avg_rating = round(total_rating / count,1)
    return avg_rating if count >0 else 0.0

def get_most_watched_genre(user_data):
    from collections import defaultdict
    dic = defaultdict(int)
    for watched_movie in user_data["watched"]:
        genre = watched_movie["genre"]
        dic[genre]+=1
    max_num = 0
    most_watched_genre = ""
    for key, value in dic.items():
        if value > max_num:
            max_num = value
            most_watched_genre = key
    return most_watched_genre if user_data["watched"] else None


    
        

    
    

    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

