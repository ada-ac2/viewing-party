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
    
    total_rating = 0
    count = 0
    for watched_movie in user_data["watched"]:
        count += 1
        total_rating += watched_movie["rating"]
    if count > 0:
        avg_rating = total_rating / count
    else:
        avg_rating = 0.0
    return avg_rating

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
    for movie in fds_watched_movies_list:
        if movie not in watched_movies_list and movie not in friends_unique_watched_movies_list:
            friends_unique_watched_movies_list.append(movie)
    return friends_unique_watched_movies_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies_list = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    user_subscriptons = user_data["subscriptions"]
    for fd_movie in friends_unique_movies:
        if fd_movie["host"] in user_subscriptons:
            recommended_movies_list.append(fd_movie["host"])
    return recommended_movies_list
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies_list_by_most_watched_genre = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    user_most_watched_genre = get_most_watched_genre(user_data)
    for fd_movie in friends_unique_movies:
        if fd_movie["genre"] == user_most_watched_genre:
             recommended_movies_list_by_most_watched_genre.append(fd_movie)
    return recommended_movies_list_by_most_watched_genre

def get_rec_from_favorites(user_data):
    
    favorite_movies_list = user_data["favorites"]

    fds_watched_movies_list= []
    for friend_data in user_data["friends"]:
        for fd_watched_movies in friend_data["watched"]:
            fds_watched_movies_list.append(fd_watched_movies)

    user_unique_favorite_movies_list = []
    for movie in favorite_movies_list:
        if movie not in fds_watched_movies_list and movie not in user_unique_favorite_movies_list:
            user_unique_favorite_movies_list.append(movie)
    return user_unique_favorite_movies_list