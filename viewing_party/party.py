# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    print("***************************")
    new_movie = {
        'title': title,
        'genre': genre,
        'rating' : rating
    }
    for value in new_movie.values():
        if value is None:
            return None
    return new_movie

def add_to_watchlist(user_data, movie):
    print("*******************************")
    if "watchlist" in user_data:
        user_data["watchlist"].append(movie)
    return user_data

def add_to_watched(user_data, movie):
    print("*******************************")
    if "watched" in user_data:
        user_data["watched"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data = add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if user_data["watched"]:
        num_of_watched = 0
        rating_sum = 0
        for movie in user_data["watched"]:
            num_of_watched+=1
            rating_sum += movie["rating"]
        return rating_sum/num_of_watched
    
    return 0

def get_most_watched_genre(user_data):
    if user_data["watched"]:
        movie_genres = {

        }
        for movie in user_data["watched"]:
            if movie['genre'] in movie_genres.keys():
                movie_genres[movie['genre']] += 1
            else:
                movie_genres[movie['genre']] = 1 
        return max(movie_genres, key=movie_genres.get)
    return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_list = []
    if user_data["watched"]:
        for movie in user_data["watched"]:
            unique_list.append(movie)
            for friend in user_data["friends"]:
                if movie in friend["watched"]: 
                    unique_list.remove(movie)
                    break
    return unique_list

def get_friends_unique_watched(user_data):
    friends_unique_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_list:
                friends_unique_list.append(movie)
    
    return friends_unique_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    available_reccomended = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            available_reccomended.append(movie)
    return available_reccomended



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

