from flask import redirect, url_for

def redirect_func(func):
    return redirect(url_for(func.__name__))