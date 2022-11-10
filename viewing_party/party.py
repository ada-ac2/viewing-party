# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    return {"title": title, "genre": genre, "rating": rating}

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
# -----------------------------------------
def get_watched_avg_rating(user_data):
    count, total_rating = 0, 0.0
    for movie in user_data["watched"]:
        count += 1
        total_rating += movie["rating"]
    return total_rating / count if count != 0 else 0.0

def get_most_watched_genre(user_data):
    # if user_data["watched"] == []: return None
    genres = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1
    sorted_genres = sorted(genres.items(), key=lambda x:x[1], reverse=True)
    return sorted_genres[0][0] if len(sorted_genres) > 0 else None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_movies, friend_movies = set(), set()

    for user_movie in user_data["watched"]:
        user_movies.add(user_movie["title"])

    for friend_dict in user_data["friends"]:
        for friend_movie in friend_dict["watched"]:
            friend_movies.add(friend_movie["title"])
    unique_title = user_movies - friend_movies

    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_title and movie not in unique_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):

    user_movies, friend_movies = set(), set()

    for user_movie in user_data["watched"]:
        user_movies.add(user_movie["title"])

    for friend_dict in user_data["friends"]:
        for friend_movie in friend_dict["watched"]:
            friend_movies.add(friend_movie["title"])
    friend_unique_titles = friend_movies - user_movies

    friend_unique_movies = []
    for friend_dict in user_data["friends"]:
        for friend_movie in friend_dict["watched"]:    
            if friend_movie["title"] in friend_unique_titles:
                if friend_movie not in friend_unique_movies:
                    friend_unique_movies.append(friend_movie)

    return friend_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    # if user_data["watched"] == []: return []
    
    streamings = set()
    for service in user_data["subscriptions"]:
        streamings.add(service)

    recommended = []
    for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie in get_friends_unique_watched(user_data):
                    if movie["host"] in streamings:
                        recommended.append(movie)

    return recommended

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_freq_genre = get_most_watched_genre(user_data) 
    rec_by_genre = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == most_freq_genre:
            rec_by_genre.append(movie)
    return rec_by_genre

def get_rec_from_favorites(user_data):
    rec_movies = []
    for fav_movie in user_data["favorites"]:
        for uniq_movie in get_unique_watched(user_data):
            if fav_movie["title"] == uniq_movie["title"]:
                rec_movies.append(fav_movie)
    return rec_movies




