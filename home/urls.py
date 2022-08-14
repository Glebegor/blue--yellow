from django.urls import path, include
from .views import homePage, LoginPage, exitPage


urlpatterns = [
    path('', homePage, name="home"),
    path('login/', LoginPage, name="login"),
    path('exit/', exitPage, name="exit")
]
