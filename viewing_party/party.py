# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title == None or genre == None or rating == None:
        return None
    else:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):

    for movie_entry in user_data["watchlist"]:
        
        if movie_entry["title"] == movie:
            user_data["watched"].append(movie_entry)
            user_data["watchlist"].remove(movie_entry)
    
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    
    if len(user_data["watched"]) != 0:
        sum = 0
    
        for movie in user_data["watched"]:
            sum += movie["rating"]
        return sum / len(user_data["watched"])
    
    else:
        return 0

def get_most_watched_genre(user_data):
    
    if len(user_data["watched"]) != 0:
        genres = {}

        for movie_entry in user_data["watched"]:
            if movie_entry["genre"] in genres:
                genres[movie_entry["genre"]] += 1
            else:
                genres[movie_entry["genre"]] = 1
        
        return max(genres, key=genres.get)
    
    else:
        return None
    
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    unique_movies = []

    if len(user_data["watched"]) != 0:
        friends_watched_titles = set()
        for friend in user_data["friends"]:
            for movie_entry in friend["watched"]:
                friends_watched_titles.add(movie_entry["title"])
        
        for movie_entry in user_data["watched"]:
            if movie_entry["title"] not in friends_watched_titles:
                unique_movies.append(movie_entry)

    return unique_movies

def get_friends_unique_watched(user_data):
    
    friends_unique_movies = []

    if len(user_data["watched"]) != 0 and len(user_data["friends"]) != 0:
        for friend in user_data["friends"]:
            for movie_entry in friend["watched"]:
                if movie_entry not in user_data["watched"] and movie_entry not in friends_unique_movies:
                    friends_unique_movies.append(movie_entry)

    return friends_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    recommendations = []

    if len(user_data["watched"]) != 0 and len(user_data["friends"]) != 0: 
        possible_recs = get_friends_unique_watched(user_data)

        recommendations = [movie for movie in possible_recs if movie["host"] in user_data["subscriptions"]]

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    possible_recs = get_available_recs(user_data)

    user_genres = set()

    for movie in user_data["watched"]:
        user_genres.add(movie["genre"])
    
    recommendations  = [movie for movie in possible_recs if movie["genre"] in user_genres]

    return recommendations

def get_rec_from_favorites(user_data):

    recommendations = []

    if len(user_data["watched"]) != 0: 
        possible_recs = get_unique_watched(user_data)

        recommendations = [movie for movie in possible_recs if movie in user_data["favorites"]]

    return recommendations

