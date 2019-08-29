from django.core.exceptions import PermissionDenied
from models import *

def checkAdmin(function):
    def wrap(request, *args, **kwargs):
        print "In wrap",request
        if request.session['user_type'] in [1,2]:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
