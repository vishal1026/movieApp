
from rest_framework import routers
from django.conf.urls import url
from .views import *

# router = routers.DefaultRouter()
# router.register(r'admin_login/', admin_login)

urlpatterns = [
    url(r'^login/', login.as_view(), name='login'),
    url(r'^admin_login/', admin_login.as_view(), name='admin_login'),
]