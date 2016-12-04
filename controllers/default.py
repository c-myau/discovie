# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import random


def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.user_id is not None: ()
    trl_list = []
    i = 0
    for row in db().select(db.yt_trailers.ALL):
        trl_list.append(row)
        i += 1
    print i
    print trl_list
    movie_list = []
    j = 0
    for row in db().select(db.test_db.ALL):
        movie_list.append(row)
        j += 1
    randm1 = []
    randm2 = []
    for x in range(0, 3):
        randm1.append(movie_list[random.randint(0, j-1)])
        randm2.append(movie_list[random.randint(0, j - 1)])
    randt = trl_list[random.randint(0,i-1)]
    print randt
    return dict(trl=trl_list, rant=randt, ranm1=randm1, ranm2 = randm2)


def userprefs():
    """Suggests movie, add like movie to database, dislike movie to database:
    """
    if auth.user_id is not None:()
    return dict()

def userprefs():
    """Suggests movie, add like movie to database, dislike movie to database:
    """
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    # Redirects user to users preference page
    auth.settings.login_next = URL('default', 'userprefs')
    #Redirects user to users preference page
    auth.settings.login_next = URL('default','userprefs')
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def directors():
    return dict()


def genres():
    return dict()


def movies():
    rows = db().select(db.test_db.ALL, limitby=(0, 100))
    return dict(rows=rows)

def createyt():
    form = SQLFORM(db.yt_trailers)
    if form.process().accepted:
        response.flash="Youtube trailer created"
    return dict(form=form)
