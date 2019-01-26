from django.db import models


class Player(models.Model):  # Darius
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    isfootball = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Team(models.Model):  # Darius
    name = models.CharField(max_length=100)
    isfootball = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)


def user_directory_path(instance, filename):
    return '{0}/{1}'.format("news_pics", filename)


class News(models.Model):  # Darius
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
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
