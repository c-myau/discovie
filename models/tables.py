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
                Field('rating', 'float', required=False),
                Field('genre', 'string', required=True),
                Field('description', 'text', required=False, default=''),
                Field('trailer_url', 'string'),
                Field('poster_url', 'upload'))

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
