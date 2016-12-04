# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

db.define_table('movie_metadata',
                Field('movie_id', 'integer', required=True),
                Field('movie_title', 'string'),
                Field('director_name', 'string'),
                Field('title_year', 'integer'),
                Field('content_rating', 'string'),
                Field('duration', 'integer'),
                Field('imdb_score', 'double'),
                Field('genres', 'string'),
                Field('plot_keywords', 'string'),
                Field('synopsis', 'text'),
                Field('gross', 'integer'),
                Field('budget', 'integer'),
                Field('color', 'string'),
                Field('aspect_ratio', 'double'),
                Field('country', 'string'),
                Field('movie_language', 'string'),
                Field('movie_facebook_likes', 'integer'),
                Field('director_facebook_likes', 'integer'),
                Field('cast_total_facebook_likes', 'integer'),
                Field('actor_1_name', 'string'),
                Field('actor_1_facebook_likes', 'integer'),
                Field('actor_2_name', 'string'),
                Field('actor_2_facebook_likes', 'integer'),
                Field('actor_3_name', 'string'),
                Field('actor_3_facebook_likes', 'integer'),
                Field('face_number_in_poster', 'integer'),
                Field('num_voted_users', 'integer'),
                Field('num_user_for_reviews', 'string'),
                Field('num_critic_for_reviews', 'integer'),
                Field('movie_poster_link', 'string'),
                Field('movie_trailer_link', 'string'),
                Field('movie_imdb_link', 'string'))

db.define_table('trailer_metadata',
                Field('movie_title', 'string', required=True),
                Field('youtube_id', 'string', required=True))

db.define_table('rating',
                Field('movie_id', 'integer', required=True),
                Field('user_id', db.auth_user, default=auth.user_id),
                Field('stars', 'integer'))

db.define_table('suggestion_list',
                Field('movie_id', 'integer', required=True),
                Field('user_id', db.auth_user, default=auth.user_id))

db.define_table('watched_list',
                Field('movie_id', 'integer', required=True),
                Field('user_id', db.auth_user, default=auth.user_id))

db.define_table('bookmark_list',
                Field('movie_id', 'integer', required=True),
                Field('user_id', db.auth_user, default=auth.user_id))


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
