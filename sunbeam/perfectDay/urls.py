from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Login'),
    path('home/<int:userID>', views.homePage, name='homePage'),
    path('forum/<int:userID>', views.forum, name='forum'),
]