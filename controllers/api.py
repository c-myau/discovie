# These are the controllers for your ajax api.
import datetime

def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])

def get_posts():
    """This controller is used to get the posts.  Follow what we did in lecture 10, to ensure
    that the first time, we get 4 posts max, and each time the "load more" button is pressed,
    we load at most 4 more posts."""
    start_index = int(request.vars.start_index) if request.vars.start_index is not None else 0
    end_index = int(request.vars.end_index) if request.vars.end_index is not None else 0
    posts = []
    has_more = False
    rows = db().select(db.post.ALL, orderby=~db.post.created_on, limitby=(start_index, end_index + 1))
    for i, r in enumerate(rows):
        if i < end_index - start_index:
            p = dict(
                id=r.id,
                user_email=r.user_email,
                user_name=get_user_name_from_email(r.user_email),
                post_content=r.post_content,
                created_on=r.created_on,
                updated_on=r.updated_on
            )
            posts.append(p)
        else:
            has_more = True
    logged_in = auth.user_id is not None
    user_email = None
    if auth.user_id is not None:
        user_id = auth.user_id
        user_email = db(db.auth_user.id == user_id).select().first().email
    return response.json(dict(
        has_more=has_more,
        logged_in=logged_in,
        posts=posts,
        user_email=user_email
    ))


# Note that we need the URL to be signed, as this changes the db.
@auth.requires_signature()
def add_post():
    """Here you get a new post and add it.  Return what you want."""
    p_id = db.post.insert(
        post_content=request.vars.post_content,
    )
    post = db.post(p_id)
    return response.json(dict(
        post=post,
    ))

@auth.requires_signature()
def edit_post():
    """Used to edit a post."""
    post_id = request.vars.post_id
    post_content = request.vars.post_content
    db(db.post.id == post_id).update(post_content=post_content, updated_on=datetime.datetime.utcnow())
    return response.json(dict(
        post=db.post(post_id)
    ))

@auth.requires_signature()
def del_post():
    """Used to delete a post."""
    db(db.post.id == request.vars.post_id).delete()
    return "Deleted"
