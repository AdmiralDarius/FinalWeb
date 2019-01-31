from django.urls import path, re_path

from . import views

app_name='sfuser'
urlpatterns = [
    path('a_player/<int:id>', views.sfuser_player, name='like_player'),
    path('a_team/<int:id>', views.sfuser_team, name='like_team'),
    path('login/', views.darius_login, name='login'),
    path('logout/', views.darius_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]
