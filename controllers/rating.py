# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import time


def index():
    return dict()


def get_info():
    rows = db().select(db.movie_metadata.ALL, orderby='<random>', limitby=(0, 8))

    def get_num_stars(movie_idx):
        if not auth.user_id:
            return None
        r = db((db.rating.user_id == auth.user_id) & (db.rating.movie_id == movie_idx)).select().first()
        return 0 if r is None else r.stars

    movie_list = []
    for i, movie in enumerate(rows):
        n = get_num_stars(i)
        movie_list.append(dict(
            url=movie.movie_poster_link,
            title=movie.movie_title,
            num_stars=n,
            num_stars_display=n,  # To facilitate vue
            id=i,
        ))
    return response.json(dict(movie_list=movie_list))


@auth.requires_signature()
def vote():
    movie_id = int(request.vars.movie_id)
    num_stars = int(request.vars.num_stars)
    db.rating.update_or_insert(
        ((db.rating.movie_id == movie_id) & (db.rating.user_id == auth.user_id)),
        movie_id=movie_id,
        user_id=auth.user_id,
        stars=num_stars
    )
    time.sleep(0.5)  # To make testing easier.
    return "ok"


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
