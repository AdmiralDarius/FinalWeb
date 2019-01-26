from django.shortcuts import render, get_object_or_404
from games import models


# Create your views here.

def all_leagues(request):
    leagues = models.League.objects.order_by("start_date")
    context = {
        "leagues": leagues,
    }
    return render(request, "Shayan/All_leagues.html", context)


def get_league(request, league_id):
    league = get_object_or_404(models.League.objects, pk=league_id)
    league_game = models.Game.objects.filter(leaguegame__in=league.leaguegame_set.all())
    if league.is_football:
        league_game = league_game.select_related('team1', 'team2', 'football_states').values(
            'team1__name', 'team2__name', 'date', 'football_states__f_score',
            'football_states__s_score', 'football_states__finished')
    else:
        league_game = league_game.select_related('team1', 'team2', 'basketball_states').values(
            'team1__name', 'team2__name', 'date', 'basketball_states__f_score',
            'basketball_states__s_score', 'basketball_states__finished')

    league_game = models.Game.objects.filter(
        leaguegame__in=league.leaguegame_set.all()).select_related('team1', 'team2',
                                                                   'football_states').all()
    league_team = league.leagueteam_set.all().values('wins', 'loses', 'team__name', 'draw',
                                                     'goals_diff', 'goals_received',
                                                     'goals_scored', 'score', 'team', 'game')

    context = {
        'league': league,
        'league_game': league_game,
        'league_team': league_team,
    }
    return render(request, "Shayan/leagues.html", context)
