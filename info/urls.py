from django.urls import path

from . import views

app_name='info'
urlpatterns = [
    path('news', views.show_news_list, name='news_list'),
    path('games', views.show_games_list, name='games_list'),
    path('a_team/<int:id>', views.a_team, name='a_team'),
    path('a_player/<int:id>', views.a_player, name='a_player'),
    path('a_team/<int:id>/<str:sortbythis>', views.a_team_sortbythis, name='team_list_sortbythis'),
]