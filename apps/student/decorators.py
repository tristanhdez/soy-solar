from functools import wraps
from flask import session, redirect


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'studentCode' in session:
            return f(*args, **kwargs)
        else:
            return redirect('login')
    return wrap
