
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/', login.as_view(), name='login'),
    url(r'^admin_login/', admin_login.as_view(), name='admin_login'),
]