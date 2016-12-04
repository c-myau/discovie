# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

import time

IMAGE_URLS = [
    'https://storage.googleapis.com/lucadealfaro-share/img1.jpg',
    'https://storage.googleapis.com/lucadealfaro-share/img2.jpg',
    'https://storage.googleapis.com/lucadealfaro-share/img3.jpg',
    'https://storage.googleapis.com/lucadealfaro-share/img4.jpg',
]


def index():
    return dict()


def get_info():
    def get_num_stars(img_idx):
        if not auth.user_id:
            return None
        r = db((db.rating.user_id == auth.user_id) & (db.rating.image_id == img_idx)).select().first()
        return 0 if r is None else r.num_stars

    image_list = []
    for i, img_url in enumerate(IMAGE_URLS):
        n = get_num_stars(i)
        image_list.append(dict(
            url=img_url,
            num_stars=n,
            num_stars_display=n,  # To facilitate vue
            id=i,
        ))
    return response.json(dict(image_list=image_list))


@auth.requires_signature()
def vote():
    picid = int(request.vars.image_id)
    num_stars = int(request.vars.num_stars)
    db.rating.update_or_insert(
        ((db.rating.image_id == picid) & (db.rating.user_id == auth.user_id)),
        image_id=picid,
        user_id=auth.user_id,
        num_stars=num_stars
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
