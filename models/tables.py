# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

db.define_table('movies',
                Field('movie_id', 'integer', required=True),
                Field('movie_name', 'string', required=True),
                Field('director', 'string', required=True),
                Field('writers', 'string', required=True),
                Field('cast_members', 'string', required=True),
                Field('mpaa_rating', 'string', required=True),
                # Field('rating', 'double', required=False),
                # Field('votes', 'double', required=False),
                Field('genre', 'string', required=True),
                Field('running_time', 'string', required=True),
                Field('description', 'text', required=False, default=''),
                Field('trailer_url', 'string'),
                Field('poster_url', 'upload'))

db.define_table('movie_metadata',
                Field('movie_id', 'integer', required=True),
                Field('color', 'string'),
                Field('director_name', 'string'),
                Field('num_critic_for_reviews', 'integer'),
                Field('duration', 'integer'),
                Field('director_facebook_likes', 'integer'),
                Field('actor_3_facebook_likes', 'integer'),
                Field('actor_2_name', 'string'),
                Field('actor_1_facebook_likes', 'integer'),
                Field('gross', 'integer'),
                Field('genres', 'string'),
                Field('actor_1_name', 'string'),
                Field('movie_title', 'string'),
                Field('num_voted_users', 'integer'),
                Field('cast_total_facebook_likes', 'integer'),
                Field('actor_3_name', 'string'),
                Field('facenumber_in_poster', 'integer'),
                Field('plot_keywords', 'string'),
                Field('movie_imdb_link', 'string'),
                Field('num_user_for_reviews', 'string'),
                Field('movie_language', 'string'),
                Field('country', 'string'),
                Field('content_rating', 'string'),
                Field('budget', 'integer'),
                Field('title_year', 'integer'),
                Field('actor_2_facebook_likes', 'integer'),
                Field('imdb_score', 'double'),
                Field('aspect_ratio', 'double'),
                Field('movie_facebook_likes', 'integer'))

db.define_table('movie_suggestions',
                Field('movie_id', 'integer', required=True),
                Field('user_id', 'integer', required=True))

db.define_table('yt_trailers',
                Field('name', 'string', required=True),
                Field('youtube_id', 'string', required=True))

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
