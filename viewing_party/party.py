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
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
   
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
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
def get_unique_watched(user_data):
    
    watched_movies_list = user_data["watched"]

    fds_watched_movies_list= []
    for friend_data in user_data["friends"]:
        for fd_watched_movies in friend_data["watched"]:
            fds_watched_movies_list.append(fd_watched_movies)

    user_unique_watched_movies_list = []
    for x in watched_movies_list:
        if x not in fds_watched_movies_list and x not in user_unique_watched_movies_list:
            user_unique_watched_movies_list.append(x)
    return user_unique_watched_movies_list

def get_friends_unique_watched(user_data):
    
    watched_movies_list = user_data["watched"]

    fds_watched_movies_list= []
    for friend_data in user_data["friends"]:
        for fd_watched_movies in friend_data["watched"]:
            fds_watched_movies_list.append(fd_watched_movies)

    friends_unique_watched_movies_list = []
    for x in fds_watched_movies_list:
        if x not in watched_movies_list and x not in friends_unique_watched_movies_list:
            friends_unique_watched_movies_list.append(x)
    return friends_unique_watched_movies_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

