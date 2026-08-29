from django.urls import path
from . import views

urlpatterns = [
    path('home/<int:userID>', views.homePage, name='homePage'),
    path('forum/<int:userID>', views.forum, name='Forum'),
]