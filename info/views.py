from django.shortcuts import render

from sfuser.models import FavouritePlayer,FavouriteTeam,FavouriteGame
from .models import News, RelateNewsTeam,RelateNewsPlayer
from games.models import RelateNewsGame, Game


def show_news_list(request):
    pages=8
    if request.POST:
        pages=int(request.POST['choice'])

    news_list=set()
    msg=""
    if request.user.is_authenticated:

        fteam=FavouriteTeam.objects.filter(user=request.user)
        fplayer = FavouritePlayer.objects.filter(user=request.user)
        fgame = FavouriteGame.objects.filter(user=request.user)

        for news in News.objects.all():
            from django.utils import timezone
            result=timezone.now() - news.date_added
            if result.days>2:
                continue
            news.day=result.days
            for team in fteam:
                if RelateNewsTeam.objects.get(news=news,team=team):
                    news_list.add(news)
            for game in fgame:
                if RelateNewsGame.objects.get(news=news,game=game):
                    news_list.add(news)
            for player in fplayer:
                if RelateNewsPlayer.objects.get(news=news,player=player):
                    news_list.add(news)

    else:
        msg="لطفا ابتدا وارد سیستم شوید تا مورد علاقه ها نمایش داده شود"


    context={"news_list":news_list,
             "msg":msg,
             "newsnumber":len(news_list),
             "football_list":News.objects.filter(isfootball=True).all().reverse()[0:pages],
             "basketball_list": News.objects.filter(isfootball=False).all().reverse()[0:pages] }

    return render(request,"Darius/news.html",context)


def show_games_list(request):
    games_list = set()
    msg = ""
    if request.user.is_authenticated:
        games_list = FavouriteGame.objects.filter(user=request.user)
    else:
        msg = "لطفا ابتدا وارد سیستم شوید تا مورد علاقه ها نمایش داده شود"

    context = {"games_list": games_list,
               "msg": msg,
               "football_list": Game.objects.filter(is_football=True).all().reverse(),
               "basketball_list": Game.objects.filter(is_football=False).all().reverse()}

    return render(request, "Darius/games.html", context)

def a_team(request,id):
    games=Game.objects.filter().all()
    context={}
    return render(request, "Darius/team.html", context)