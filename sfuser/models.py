from django.db import models
from django.contrib.auth.models import User
from info.models import Team,Player,News
from games.models import Game

class FavouriteGame(models.Model):  # Darius
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class FavouritePlayer(models.Model):  # Darius
    player=models.ForeignKey(Player, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class FavouriteTeam(models.Model):  # Darius
    team=models.ForeignKey(Team, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class SFComment(models.Model):  # shayan

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    text = models.CharField(max_length=400)
    date = models.DateTimeField()
