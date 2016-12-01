def get_movie_genre():
    genre = request.args[0]
    rows = db(db.director == genre).select()
    return dict(row=rows)


def get_movie_directors():
    director = request.args[0]
    rows = db(db.director == director).select()
    return dict(row=rows)


def get_movie_category():
    category = request.args[0]
    rows = db(db.movie.genre == category).select()
    return dict(rows=rows)


def search():
    return dict()
