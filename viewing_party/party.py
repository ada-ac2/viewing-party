# ------------- WAVE 1 --------------------

# wave 1 fun 1
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dic ={
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_dic
    else:
        return None

# wave 1 fun 2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# wave 1 fun 3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# wave 1 fun 4 
def watch_movie(user_data, movie_title):
    print(f"user_data: {user_data} \n movie_title: {movie_title}")
    # if title not in the watchlist => return data
    for movie_dic in user_data["watchlist"]:
        print(f"movie_dic: {movie_dic}")
        print(f"movie_dic['title']: {movie_dic['title']}")
        # if title in the watchlist => remove it
        if movie_dic["title"] == movie_title:
            # add to watched_list
            user_data["watched"].append(movie_dic)
            user_data["watchlist"].remove(movie_dic)
    # return data
    print(f"final user_data: {user_data}")
    print(len(user_data["watchlist"]))
    print(len(user_data["watched"]))
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# wave 2 fun 1
def get_watched_avg_rating(user_data):
    # if user_data["watched"] length is 0
    # return 0.0 as average
    # else add the sum of the all rating and devide by length
    # return average
    average = 0.0
    if len(user_data["watched"]) == 0:
        return average
    else:
        sum = 0
        for movie_dic in user_data["watched"]:
            sum += movie_dic["rating"]
        average = sum / len(user_data["watched"])
    return average

# wave 2 fun 2
def get_most_watched_genre(user_data):
    # if length of user_data["watched"] is 0 return None
    # else set a counter_dic and max_num 
    # to count the genre
    if len(user_data["watched"]) == 0:
        return None
    else:
        counter_dic = {}
        for movie_dic in user_data["watched"]:
            key = movie_dic["genre"]
            if key in counter_dic:
                counter_dic[key] += 1
            else:
                counter_dic[key] = 1
        
        max_num = 0
        for num in counter_dic.values():
            if num > max_num:
                max_num = num

        max_genre = list(counter_dic.keys())[list(counter_dic.values()).index(max_num)]
        return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# wave 3 fun 1
def get_unique_watched(user_data):
    # return a list of dictionaries that contain movies 
    # which friends' didn't watched
    # print(f"user: {user_data['watched']}")
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    # print(f"user_watched_set: {user_watched_set}")
    friends_watched_set = set()
    for friend_watched in user_data["friends"]:
        for movie_name in friend_watched["watched"]:
            friends_watched_set.add(movie_name["title"])
    # print(f"friends_watched_set: {friends_watched_set}")
    non_watch_set = user_watched_set.difference(friends_watched_set)
    # print(f"none_watch_set: {none_watch_set}")
    non_watched_list = []
    for name in list(non_watch_set):
        for movie in user_data["watched"]:
            if name == movie["title"]:
                non_watched_list.append(movie)
    # print(f"non_watched_list: {non_watched_list}")
    return non_watched_list 
#wave 3 fun 2
def get_friends_unique_watched(user_data):
    # print(f"user_data[watch]: {user_data['watched']}")
    # print("******************************************")
    # print(f"user_data[firends]: {user_data['friends']}")
    # print("******************************************")
    #user watched set
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    # friends watch set
    friends_watched_set = set()
    for friend_watched in user_data["friends"]:
        for movie_name in friend_watched["watched"]:
            friends_watched_set.add(movie_name["title"])
    #friends watched but user's didn't
    user_nonwatched_set = friends_watched_set.difference(user_watched_set)
    # print(f"user_nonwatched_set: {user_nonwatched_set}")
    # print("******************************************")
    # create the result list to store
    # use title value to find the movie dictionaries and store them to the result list
    result_list =[]
    for name in list(user_nonwatched_set):
        for friends_movie in user_data["friends"]:
            for movie in friends_movie["watched"]:
                if name == movie["title"] and result_list.count(movie)==0 :
                    result_list.append(movie)
    # print(f"result_list: {result_list}")
    return result_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # return a recommended movies list
    # conditions:
    # user didn't watch but friend watched
    # match the user's subscriptions list
    # may use  get_friends_unique_watched(user_data) to return a user non_watched list
    user_nonwatched_list = get_friends_unique_watched(user_data)
    user_subscriptions_list = user_data["subscriptions"]
    recommended_movies_list = []
    for movie in user_nonwatched_list:
        for host_name in user_subscriptions_list:
            if movie["host"] == host_name:
                recommended_movies_list.append(movie)
    return recommended_movies_list
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    # return a recommended movies list
    # conditions:
    # user didn't watch but friends watched
    # The "genre" match the user's most frequent genre
    # may use get_most_watched_genre() to get the most frequent genre
    # and use get_friends_unique_watched() to get a user non_watched list
    max_genre = get_most_watched_genre(user_data)
    user_nonwatched_list = get_friends_unique_watched(user_data)
    recommended_movies_list = []
    for movie in user_nonwatched_list:
        if movie["genre"] == max_genre:
            recommended_movies_list.append(movie)
    return recommended_movies_list 

def get_rec_from_favorites(user_data):
    # return a recommended movies list 
    # conditions:
    # user favorites but friends haven't watched
    # print(f"user_data: {user_data}")
    user_favorites_set = set()
    for user_favorites in user_data["favorites"]:
        user_favorites_set.add(user_favorites["title"])
    # print(f"user_favorites_set: {user_favorites_set}")

    friends_watched_set = set()
    for friend_watched in user_data["friends"]:
        for movie_name in friend_watched["watched"]:
            friends_watched_set.add(movie_name["title"])
    # print(f"friends_watched_set: {friends_watched_set}")       
    
    friends_nonwatch_set = user_favorites_set.difference(friends_watched_set)
    # print(f"friends_nonwatch_set: {friends_nonwatch_set}")  
    recommended_list = []
    for name in list(friends_nonwatch_set):
        for movie in user_data["favorites"]:
            if name == movie["title"]:
                recommended_list.append(movie)
        
    # print(f"recommended_list: {recommended_list}")  

    return recommended_list