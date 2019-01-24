from django.urls import path

from . import views

app_name='info'
urlpatterns = [
    path('news', views.show_news_list, name='news_list'),
    path('games', views.show_games_list, name='games_list'),
]