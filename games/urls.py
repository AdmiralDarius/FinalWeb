from django.urls import path, re_path

from . import views


urlpatterns = [
    path(r'all_leagues/', views.all_leagues, name='all leagues'),
    path(r'league/<int:league_id>', views.get_league, name='league'),
    path(r'all_leagues/search', views.all_leagues_search, name='league_search'),

]
