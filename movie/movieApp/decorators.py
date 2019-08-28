from django.core.exceptions import PermissionDenied
from models import *

def checkAdmin(function):
    def wrap(request, *args, **kwargs):
        if request.session['user_type'] == 1 or request.session['user_type'] == 2:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
