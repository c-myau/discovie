# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('DISC', SPAN('ovie')), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href=URL('default', 'index'),
                  _id="discovie-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # genres = ['Action', 'Adventure', 'Fantasy', 'Sci-Fi', 'Thriller', 'Documentary', 'Romance', 'Animation', 'Comedy',
    #           'Family', 'Musical', 'Mystery', 'Western', 'Drama', 'History', 'Sport', 'Crime', 'Horror', 'War',
    #           'Biography', 'Music', 'Game-Show', 'Reality-TV', 'News', 'Short', 'Film-Noir']
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('Movies'), False, URL('discovie', 'default', 'movies')),
        (T('Popular'), False, URL('discovie', 'default', 'popular')),
        (T('Top'), False, URL('discovie', 'default', 'top')),
        (T('Genres'), False, '#', [
            (T('Action'), False, URL('discovie', 'default', 'genres', args=['Action'])),
            (T('Adventure'), False, URL('discovie', 'default', 'genres', args=['Adventure'])),
            (T('Fantasy'), False, URL('discovie', 'default', 'genres', args=['Fantasy'])),
            (T('Sci-Fi'), False, URL('discovie', 'default', 'genres', args=['Sci-Fi'])),
            (T('Thriller'), False, URL('discovie', 'default', 'genres', args=['Thriller'])),
            (T('Documentary'), False, URL('discovie', 'default', 'genres', args=['Documentary'])),
            (T('Romance'), False, URL('discovie', 'default', 'genres', args=['Romance'])),
            (T('Animation'), False, URL('discovie', 'default', 'genres', args=['Animation'])),
            (T('Comedy'), False, URL('discovie', 'default', 'genres', args=['Comedy '])),
            (T('Family'), False, URL('discovie', 'default', 'genres', args=['Family'])),
            (T('Musical'), False, URL('discovie', 'default', 'genres', args=['Musical'])),
            (T('Mystery'), False, URL('discovie', 'default', 'genres', args=['Mystery'])),
            (T('Western'), False, URL('discovie', 'default', 'genres', args=['Western'])),
            (T('Drama'), False, URL('discovie', 'default', 'genres', args=['Drama'])),
            (T('History'), False, URL('discovie', 'default', 'genres', args=['History'])),
            (T('Sport'), False, URL('discovie', 'default', 'genres', args=['Sport'])),
            (T('Crime'), False, URL('discovie', 'default', 'genres', args=['Crime'])),
            (T('Horror'), False, URL('discovie', 'default', 'genres', args=['Horror'])),
            (T('War'), False, URL('discovie', 'default', 'genres', args=['War'])),
            (T('Biography'), False, URL('discovie', 'default', 'genres', args=['Biography'])),
            (T('Music'), False, URL('discovie', 'default', 'genres', args=['Music'])),
            (T('Game-Show'), False, URL('discovie', 'default', 'genres', args=['Game-Show'])),
            (T('Reality-TV'), False, URL('discovie', 'default', 'genres', args=['Reality-TV'])),
            (T('News'), False, URL('discovie', 'default', 'genres', args=['News'])),
            (T('Short'), False, URL('discovie', 'default', 'genres', args=['Short'])),
            (T('Film-Noir'), False, URL('discovie', 'default', 'genres', args=['Film-Noir'])),
        ]),
        # (T('This App'), False, '#', [
        #     (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
        #     LI(_class="divider"),
        #     (T('Controller'), False, URL('admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
        #     (T('View'), False, URL('admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
        #     (T('DB Model'), False, URL('admin', 'default', 'edit/%s/models/db.py' % app)),
        #     (T('Menu Model'), False, URL('admin', 'default', 'edit/%s/models/menu.py' % app)),
        #     (T('Config.ini'), False, URL('admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
        #     (T('Layout'), False, URL('admin', 'default', 'edit/%s/views/layout.html' % app)),
        #     (T('Stylesheet'), False, URL('admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
        #     (T('Database'), False, URL(app, 'appadmin', 'index')),
        #     (T('Errors'), False, URL('admin', 'default', 'errors/' + app)),
        #     (T('About'), False, URL('admin', 'default', 'about/' + app)),
        # ]),
    ]

if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
