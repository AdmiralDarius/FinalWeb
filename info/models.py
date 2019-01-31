from django.db import models





class Team(models.Model):  # Darius
    name = models.CharField(max_length=100)
    isfootball = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

def player_pic_path(instance, filename):
    return '{0}/{1}'.format("player_pics", filename)

class Player(models.Model):  # Darius
    picture = models.ImageField(upload_to=player_pic_path, null=True, blank=True)
    age = models.IntegerField()
    pheight= models.IntegerField()
    pweight= models.IntegerField()
    nationality=models.CharField(max_length=100)
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



class SeasonFootball(models.Model):
    season_number=models.IntegerField(unique=True)
    player=models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    goals=models.IntegerField()
    pas=models.IntegerField()
    fouls=models.IntegerField()
    carts=models.IntegerField()
    game_time=models.IntegerField()

    class Meta:
        ordering = ["season_number"]

class SeasonBasketball(models.Model):
    season_number = models.IntegerField(unique=True)
    player=models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    partab2=models.IntegerField()
    partab3=models.IntegerField()
    fouls = models.IntegerField()
    rebound= models.IntegerField()
    game_time = models.IntegerField()

    class Meta:
        ordering = ["season_number"]