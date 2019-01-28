from django.db import models
from info.models import Team, Player


class BasketbalState(models.Model):  # shayan
    # "f" for team1 and "s" for team2

    finished = models.BooleanField()
    f_total_score = models.IntegerField()
    s_total_score = models.IntegerField()
    f_2points_shots = models.IntegerField()
    s_2points_shots = models.IntegerField()
    f_3points_shots = models.IntegerField()
    s_3points_shots = models.IntegerField()
    f_fouls = models.IntegerField()
    s_fouls = models.IntegerField()
    f_penalties = models.IntegerField()
    s_penalties = models.IntegerField()
    f_rebounds = models.IntegerField()
    s_rebounds = models.IntegerField()
    f_1st_quarter_score = models.IntegerField()
    s_1st_quarter_score = models.IntegerField()
    f_2nd_quarter_score = models.IntegerField()
    s_2nd_quarter_score = models.IntegerField()
    f_3rd_quarter_score = models.IntegerField()
    s_3rd_quarter_score = models.IntegerField()
    f_4th_quarter_score = models.IntegerField()
    s_4th_quarter_score = models.IntegerField()


class League(models.Model):  # shayan

    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=200)
    is_football = models.BooleanField()
    start_date = models.DateField()
    finished = models.BooleanField()


class FootballState(models.Model):  # shayan

    # "f" for team1 and "s" fo team2

    finished = models.BooleanField()
    f_score = models.IntegerField()
    s_score = models.IntegerField()
    f_corner = models.IntegerField()
    s_corner = models.IntegerField()
    f_chances = models.IntegerField()
    s_chances = models.IntegerField()
    f_possession = models.IntegerField()
    s_possession = models.IntegerField()


class LeagueTeam(models.Model):  # shayan

    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')
    wins = models.IntegerField()
    loses = models.IntegerField()
    draw = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_received = models.IntegerField()
    goals_diff = models.IntegerField()
    score = models.IntegerField()
    game = models.IntegerField()


def user_directory_path(instance, filename):
    return '{0}/{1}'.format("games_pics", filename)


class Game(models.Model):  # shayan
    
    title = models.CharField(max_length=50)
    brief_description = models.CharField(max_length=100)
    stadium = models.CharField(max_length=50)

    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1_reverse",
                              null=True, blank=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2_reverse",
                              null=True, blank=True)
    is_football = models.BooleanField()
    football_states = models.ForeignKey(FootballState, on_delete=models.CASCADE, null=True,
                                        blank=True)
    basketball_states = models.ForeignKey(BasketbalState, on_delete=models.CASCADE, null=True,
                                          blank=True)
    date = models.DateTimeField()
    week = models.IntegerField()
    best_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)


class LeagueGame(models.Model):  # shayan

    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)


class Event(models.Model):  # shayan

    event_choices = (

        ('ec', 'exchange'),

        # football
        ('rc', 'red card'),
        ('yc', 'yellow card'),
        ('go', 'goal'),

        # basketball
        ('rb', 'rebound'),
        ('2p', '2 point'),
        ('3p', '3 point'),

    )

    color_choices = (
        ('ec', 'table-info'),

        # football
        ('rc', 'bg-danger'),
        ('yc', 'table-danger'),
        ('go', 'bg-success'),

        # basketball
        ('rb', 'table-danger'),
        ('2p', 'table-success'),
        ('3p', 'bg-success'),

    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='events')
    title = models.CharField(max_length=2, choices=event_choices)
    time = models.TimeField()
    event_pic = models.CharField(max_length=30)
    first_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='first_player')
    second_player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='second_player')
    event_color_class = models.CharField(max_length=4, null=True, blank=True, choices=color_choices)


class RelateNewsGame(models.Model):  # Darius
    from info.models import News

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
