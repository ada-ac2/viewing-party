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
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data 

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data  


# ----------------------------------------- 
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    count = 0
    sum_movie_rating = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie in user_data["watched"]:
        sum_movie_rating += movie["rating"]
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
    friend_all_watched = []
    for i in range(len(friend_lst)):
        friend_all_watched.extend(friend_lst[i]["watched"])

    for j in range(len(user_data_watched_lst)):
        if user_data_watched_lst[j] not in friend_all_watched:
            delete_movie = user_data_watched_lst[j]
            unique_movie_lst.append(delete_movie)
    return unique_movie_lst


def get_friends_unique_watched(user_data):
    user_data_watched_lst = user_data["watched"]
    friend_lst = user_data["friends"]
    #all_watched = []
    friend_unique_lst = []
    for friend in friend_lst:
        for movie in friend["watched"]:
            if movie not in friend_unique_lst:
                friend_unique_lst.append(movie)

    for j in range(len(user_data_watched_lst)):
        if user_data_watched_lst[j] in friend_unique_lst:
            friend_unique_lst.remove(user_data_watched_lst[j])
    return friend_unique_lst
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
# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    recommended_by_genre = []
    most_genre = get_most_watched_genre(user_data)
    recommended_lst = get_friends_unique_watched(user_data)
   
    for i in range(len(recommended_lst)):
        if recommended_lst[i]["genre"] == most_genre:
            recommended_by_genre.append(recommended_lst[i])
    return recommended_by_genre


def get_rec_from_favorites(user_data):
    user_unique = get_unique_watched(user_data)
    favorites_lst = []
    for i in user_data["favorites"]:
        if i in user_unique:
            favorites_lst.append(i)
    return favorites_lst





# -----------------------------------------

