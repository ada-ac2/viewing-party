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
    # if len(user_data["watched"])==0:
    user_data["watched"].append(movie)
    return user_data

# wave 1 fun 3
def add_to_watchlist(user_data, movie):
    # if len(user_data["watchlist"])==0:
    user_data["watchlist"].append(movie)
    return user_data

# wave 1 fun 4 (questions)
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
    pass
#wave 3 fun 2
def get_friends_unique_watched(user_data):
    pass
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

