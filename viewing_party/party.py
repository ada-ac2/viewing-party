# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    movies = {}

    if movie_title == None or genre == None or rating == None :
        return None

    movies["title"] = movie_title
    movies["genre"] = genre
    movies["rating"] = rating

    return movies

movie_title = "MOVIE_TITLE_1"
genre = "GENRE_1"
rating = "RATING_1"

# print(create_movie(movie_title, genre, rating))

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# movie = {
#     "title": "MOVIE_TITLE_1",
#     "genre": "GENRE_1",
#     "rating": "RATING_1"
# }
# user_data = {
#     "watched": []
# }

# print(add_to_watched(user_data, movie))



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

