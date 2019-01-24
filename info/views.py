from django.shortcuts import render

from sfuser.models import FavouritePlayer,FavouriteTeam,FavouriteGame
from .models import News, RelateNewsTeam,RelateNewsPlayer
from games.models import RelateNewsGame


def show_news_list(request):
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
             "football_list":News.objects.filter(isfootball=True).all().reverse()[0:8],
             "basketball_list": News.objects.filter(isfootball=False).all().reverse()[0:8] }

    return render(request,"Darius/news.html",context)