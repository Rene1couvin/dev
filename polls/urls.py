from django.urls import path
# from .views import udetail
from .views import *

urlpatterns =[
    # path("users/", udetail.as_view(), name="users"),
    path("", home, name="home"),
    path("home", home, name="home"),
    path("ahome", ahome, name="ahome"),
    path("reserve", reserve, name="reserve"),
    path('add/', add, name='add'),    
    path("login/", login_view, name="login"),
    path("signup/", signup, name="signup"),
    path('logout/', logout_view, name='logout'),   
    path('profile/', profile_view, name='profile'),
    path('parkingplace', parkingplace, name="parkingplace"),
    path('parkingg', parking_places_list, name='parkingg'),
    path('reservess/<int:pk>', reserves, name='reservess'),
]
