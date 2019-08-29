
from rest_framework import routers
from django.conf.urls import url
from .views import *

# router = routers.DefaultRouter()
# router.register(r'admin_profile/', admin_profile)

urlpatterns = [
    url(r'^login/', login.as_view(), name='login'),
    url(r'^admin_profile/', admin_profile, name='admin_profile'),
    url(r'^add_admin/', add_admin, name='add_admin'),
    url(r'^logout_user/', logout_user, name='logout_user'),
]