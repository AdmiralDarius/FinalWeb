from django.db import models
from info.models import News


class FavouriteGame(models.Model):  # Darius
    pass


class FavouritePlayer(models.Model):  # Darius
    pass


class FavouriteTeam(models.Model):  # Darius
    pass


class SFComment(models.Model):  # shayan

    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    text = models.CharField(max_length=400)
    date = models.DateTimeField()
