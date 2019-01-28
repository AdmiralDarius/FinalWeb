from django.db import models
from games.models import Game





class Team(models.Model):  # Darius
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    isfootball = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

class Player(models.Model):  # Darius
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    isfootball = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    team=models.ForeignKey(Team, on_delete=models.CASCADE)

def user_directory_path(instance, filename):
    return '{0}/{1}'.format("news_pics", filename)


class News(models.Model):  # Darius
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    source = models.CharField(max_length=100)
    isfootball = models.BooleanField(default=True)

    class Meta:
        ordering = ["date_added"]


class RelateNewsTeam(models.Model):  # Darius
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class RelateNewsPlayer(models.Model):  # Darius
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):  # Darius
    news = models.ManyToManyField(News)
    description = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)


def game_pic_directory(instance, filename):
    return '{0}/{1}/{2}'.format('game pictures', instance.game_id, filename)


class GamePic(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to=game_pic_directory, null=True, blank=True)


def game_video_directory(instance, filename):
    return '{0}/{1}/{2}'.format('game videos', instance.game_id, filename)


class GameVideo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to=game_video_directory, null=True, blank=True)
