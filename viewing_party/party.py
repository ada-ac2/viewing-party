#from collections import Counter
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
def get_watched_avg_rating(user_data):
    count = 0
    sum_movie_rating = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    
    for i in range(len(user_data["watched"])):
        sum_movie_rating += user_data["watched"][i]["rating"]
        count += 1
    average_rating = sum_movie_rating / count
    return average_rating


def get_most_watched_genre(user_data):
    
    genre_dict = {}
    if len(user_data["watched"]) == 0:
        return None
    
    for i in range(len(user_data["watched"])):
        genre = user_data["watched"][i]["genre"]
        genre_dict[genre] = genre_dict.get(genre, 0) + 1
    
    genre_dict = sorted(genre_dict.items(), key = lambda item: item[1], reverse = True)
    return genre_dict[0][0]


# -----------------------------------------
# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    user_data_watched_lst = user_data["watched"]
    friend_lst = user_data["friends"]
    unique_movie_lst = []
    all_watched = []
    for i in range(len(friend_lst)):
        all_watched.extend(friend_lst[i]["watched"])

    for j in range(len(user_data_watched_lst)):
        if user_data_watched_lst[j] not in all_watched:
            delete_movie = user_data_watched_lst[j]
            unique_movie_lst.append(delete_movie)
    return unique_movie_lst


def get_friends_unique_watched(user_data):
    user_data_watched_lst = user_data["watched"]
    friend_lst = user_data["friends"]
    all_watched = []
    friend_unique_list = []
    for i in range(len(friend_lst)):
        all_watched.extend(friend_lst[i]["watched"])
    print(all_watched)
    print(len(all_watched))
    for i in range(len(all_watched)):
        if all_watched[i] not in friend_unique_list:
            friend_unique_list.append(all_watched[i])
    for j in range(len(user_data_watched_lst)):
        if user_data_watched_lst[j] in friend_unique_list:
            friend_unique_list.remove(user_data_watched_lst[j])
    return friend_unique_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    recommended_lst = []
    friend_unique_lst = get_friends_unique_watched(user_data)
    for i in range(len(friend_unique_lst)):
        if friend_unique_lst[i]["host"] in user_data["subscriptions"]:
            recommended_lst.append(friend_unique_lst[i])
    return recommended_lst


    



# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

