from django.urls import path, re_path

from . import views


urlpatterns = [
    path(r'all_leagues/', views.all_leagues, name='all leagues'),
    re_path(r'^league/(?P<league_id>[0-9]+)$', views.get_league, name='league'),
    path(r'all_leagues/search', views.all_leagues_search, name='league_search'),

]
