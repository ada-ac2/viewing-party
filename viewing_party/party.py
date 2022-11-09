# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title == None or genre == None or rating == None:
        return None

    movie_dict = {
        "title": title ,
        "genre": genre ,
        "rating": rating
        }
    return movie_dict
    
#++++++++
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    print(user_data)
    return user_data
#++++++++++++
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    print(user_data)
    return user_data
#+++++++++++++++
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
###### WAve 2#################
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    total = 0
    for movie in user_data["watched"]:
        total += movie["rating"]
    avg_rating = total / len(user_data["watched"])
    return avg_rating 

### +++++++++++++++++++
def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_their_freq_in_userdata = {}
    for movie in user_data["watched"]:
        this_genre = movie["genre"]
        if this_genre not in genre_their_freq_in_userdata.keys():
            genre_their_freq_in_userdata[this_genre] = 1
        else:
            genre_their_freq_in_userdata[this_genre] += 1
        popular_genre_freq = 0
        for genre in genre_their_freq_in_userdata:
            genre_freq = genre_their_freq_in_userdata[genre]
            if genre_freq > popular_genre_freq:
                popular_genre = genre
                popular_genre_freq = genre_freq
    return popular_genre

#### +++++++++++++++++++++++++
# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    friends_movie_list = []
    for friends_watched_movie in user_data["friends"]:
        for movie in friends_watched_movie["watched"]:
            friends_movie_list.append(movie)
    #print(friends_movie_list)
    my_unique_watched_list = []
    for my_unique_movie in user_data["watched"]:
        if my_unique_movie not in friends_movie_list and my_unique_movie not in my_unique_watched_list:
            my_unique_watched_list.append(my_unique_movie)
    #print(my_unique_watched_list)
    return my_unique_watched_list
###+++++++++++++++++++++

def get_friends_unique_watched(user_data):
    friends_unique_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movie:
                friends_unique_movie.append(movie)
    #print(friends_unique_movie)
    return friends_unique_movie

###### Wave 4++++++++++++++++++++++++++++
def get_available_recs(user_data):
    friends_unique_watched_movies = get_friends_unique_watched(user_data)
    recommended_movies_for_me = []
    for movie in friends_unique_watched_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies_for_me.append(movie)
    return recommended_movies_for_me

###++++++++++++Wave 5 ++++++++++++++++

def get_new_rec_by_genre(user_data):
    popular_genre = get_most_watched_genre(user_data)
    friends_unique_watched_movies = get_friends_unique_watched(user_data)
    recommended_movies_by_genre = []

    for movie in friends_unique_watched_movies:
        if movie["genre"] == popular_genre:
            recommended_movies_by_genre.append(movie)
    return recommended_movies_by_genre
######++++++++++++++++++++++++++
def get_rec_from_favorites(user_data):
    friends_movie_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_list.append(movie)

    recommended_movies_by_favorites = []

    for movie in user_data["favorites"]:
        if movie not in friends_movie_list:
            recommended_movies_by_favorites.append(movie)

    return recommended_movies_by_favorites

