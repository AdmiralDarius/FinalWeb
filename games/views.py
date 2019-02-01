from django.shortcuts import render, get_object_or_404
from games import models
from info.views import get_related_news


# Create your views here.

def all_leagues(request):
    leagues = models.League.objects.order_by("start_date")
    context = {
        "leagues": leagues,
    }
    return render(request, "Shayan/All_leagues.html", context)


def all_leagues_search(request):
    leagues = models.League.objects.order_by("start_date")
    result = []
    for league in leagues:
        if request.POST['query'] in league.name:
            result.append(league)

    context = {
        "leagues": result,
    }
    return render(request, "Shayan/All_leagues.html", context)


def get_league(request, league_id):
    league = get_object_or_404(models.League.objects, pk=league_id)
    league_game = models.Game.objects.filter(leaguegame__in=league.leaguegame_set.all())
    if league.is_football:
        league_game = league_game.select_related('team1', 'team2', 'football_states').values(
            'team1__name', 'team2__name', 'date', 'football_states__f_score',
            'football_states__s_score', 'football_states__finished', 'week')
    else:
        league_game = league_game.select_related('team1', 'team2', 'basketball_states').values(
            'team1__name', 'team2__name', 'date', 'basketball_states__f_score',
            'basketball_states__s_score', 'basketball_states__finished', 'week')

    league_team = league.leagueteam_set.all().values('wins', 'loses', 'team__name', 'draw',
                                                     'goals_diff', 'goals_received',
                                                     'goals_scored', 'score', 'team', 'game')

    relation = [team.name for team in league_team]
    relation.append(league.name)
    related_news = get_related_news(*relation)[:4]
    context = {
        'league': league,
        'league_game': league_game,
        'league_team': league_team,
        'related_news': related_news,
    }
    return render(request, "Shayan/leagues.html", context)
