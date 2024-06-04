from django.urls import path
# from .views import udetail
from .views import *

urlpatterns =[
    # path("users/", udetail.as_view(), name="users"),
    path("", home, name="home"),
    path("home", home, name="home"),
    path("ahome", ahome, name="ahome"),
    path("reserve", reserve, name="reserve"),
    path("about", about, name="about"),
    path("service", service, name="service"),
    path("login/", login_view, name="login"),
    path("signup/", signup, name="signup"),
    path("contact/", contact, name="contact"),
    path('logout/', logout_view, name='logout'),   
    path('profile/', profile_view, name='profile'),
]
