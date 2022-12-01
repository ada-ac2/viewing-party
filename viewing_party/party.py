from collections import defaultdict

# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if title and genre and rating:
        ans = {"title": title, "genre": genre, "rating": rating}
        return ans
    return None


def add_to_watched(user_data, movie):
    # TODO: Should we check if the movie is already in watched_movies?
    watched_movies = user_data["watched"]  # watched_movies is a list of dictionaries.
    watched_movies.append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    # TODO: Should we check if the movie is already in the watchlist?
    movie_watchlist = user_data["watchlist"] # movie_watchlist is a list of dictionaries.
    movie_watchlist.append(movie)
    return user_data


def watch_movie(user_data, title):
    movie_watchlist = user_data["watchlist"]
    # TODO: Should we check if the movie has already been watched?
    for index, movie in enumerate(movie_watchlist):
        movie_title = movie["title"]
        if title == movie_title:
            add_to_watched(user_data, movie)
            movie_watchlist[index], movie_watchlist[-1] = movie_watchlist[-1], movie_watchlist[index]
            movie_watchlist.pop()  # considered time complexity, switch the element with last one and pop.
            return user_data
    return user_data   # not found


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0.0
    amount = 0
    watched_movies = user_data["watched"]
    for movie in watched_movies:
        rating = movie["rating"]
        amount += 1
        total_rating += rating
    if amount:  # avoid ZeroDivisionError
        return total_rating / amount
    return total_rating


def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    genre_map = defaultdict(int)
    for movie in watched_movies:
        genre = movie["genre"]
        genre_map[genre] += 1
    most_watched_genre = None
    max_amount = 0
    for genre, times in genre_map.items():
        # if there is a tie, keep the first
        if times > max_amount:
            max_amount = times
            most_watched_genre = genre
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# return a dictionary, key is title, value is a dictionary of movie's information
def get_friends_watched_movies(friends):
    watched_movies = {}
    for friend in friends:
        watched_movies_of_friend = friend["watched"]  # a list of watched movies
        for friends_movie in watched_movies_of_friend:  # each friends_movie is a dictionary
            title = friends_movie["title"]
            if title not in watched_movies:
                watched_movies[title] = friends_movie
    return watched_movies


def get_unique_watched(user_data):
    watched_movies = user_data["watched"]
    ans = []
    friends = user_data["friends"]
    friends_watched_movies = get_friends_watched_movies(friends)
    for watched_movie in watched_movies:
        title = watched_movie["title"]
        if title not in friends_watched_movies:
            ans.append(watched_movie)
    return ans


def get_friends_unique_watched(user_data):
    friends = user_data["friends"]
    watched_movies = user_data["watched"]
    user_watched = set()
    for watched_movie in watched_movies:
        title = watched_movie["title"]
        user_watched.add(title)
    friends_watched_movies = get_friends_watched_movies(friends)
    ans = []
    for title, friends_watched_movie in friends_watched_movies.items():
        if title not in user_watched:
            ans.append(friends_watched_movie)
    return ans

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_subscriptions = set()
    for subscription in user_data["subscriptions"]:
        available_subscriptions.add(subscription)
    candidates = get_friends_unique_watched(user_data)
    recommendations = []
    for candidate in candidates:
        if candidate["host"] in available_subscriptions:
            recommendations.append(candidate)
    return recommendations



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommendations = []
    candidates = get_friends_unique_watched(user_data)
    most_genre = get_most_watched_genre(user_data)

    # if the most_genre is None
    if most_genre is None:
        return recommendations

    for candidate in candidates:
        if candidate["genre"] == most_genre:
            recommendations.append(candidate)
    return recommendations


def get_rec_from_favorites(user_data):  # assume user already watched favorite_movies
    favorite_movies = user_data["favorites"]
    recommendations = []
    friends = user_data["friends"]
    already_watched = get_friends_watched_movies(friends)
    for candidate in favorite_movies:
        if candidate["title"] not in already_watched:
            recommendations.append(candidate)
    return recommendations

