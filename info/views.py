from django.shortcuts import render, get_object_or_404

from sfuser.models import FavouritePlayer, FavouriteTeam, FavouriteGame
from .models import News, RelateNewsTeam, RelateNewsPlayer, Tag, Team, Player
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
    news_list = set()
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


def get_news(request, news_id):
    news = get_object_or_404(News.objects, pk=news_id)
    tag = news.tag_set.all()
    context = {
        'news': news,
        'tags': tag,
    }

    return render(request, 'Shayan/news_page.html', context)


def get_game(request, game_id):
    game = get_object_or_404(
        Game.objects.select_related('best_player').prefetch_related(
            'gamepic_set', 'gamevideo_set', 'basketball_states', 'football_states',
            'team1__players',
            'team2__players', 'events__first_player', 'events__second_player', ), pk=game_id)
    team1_players = game.team1.players.all()
    team1_players = game.team2.players.all()
    events = game.events.select_related('first_player', 'second_player')
    state = None
    bestPlayer = game.best_player
    pics = game.gamepic_set
    videos = game.gamevideo_set
    if game.is_football:
        state = game.football_states
    else:
        state = game.basketball_states
    # context = {
    #     'game':game,
    #     'team1_palyer'
    # }

def a_team(request,id):
    team=Team.objects.get(id=id)
    games=Game.objects.filter(Q(team1=team)|Q(team2=team)).all()
    context={"team":team,"games":games}
    return render(request, "Darius/team.html", context)

def a_team_sortbythis(request,id,sortbythis):
    team=Team.objects.get(id=id)

    raw_news=News.objects.all()
    final_news=[]
    for now in raw_news:
        cur_tex=now.body+now.title
        for i in now.tag_set.all():
            cur_tex+=i.description
        if team.name in cur_tex:
            final_news.append(now)
            continue
        for i in team.player_set.all():
            if i.name in cur_tex:
                final_news.append(now)
                continue

    games_final=[]

    raw_games=Game.objects.filter(Q(team1=team)|Q(team2=team)).all()
    for game in raw_games:
        tmp={}
        result='مساوی'
        if game.team1==team:
            tmp['team']=game.team2
            tmp['result'] = game.result
        else:
            tmp['team'] = game.team1
            if game.result=="برد" :
                result="باخت"
            if game.result=="باخت" :
                result="برد"
            tmp['result'] = game.result
        tmp['date']=game.date
        games_final.append(tmp)

    if sortbythis=='date':
        games_final.sort(key=lambda x:x.date)
    if sortbythis=='opponent':
        games_final.sort(key=lambda x:x.team)
    if sortbythis=='result':
        games_final.sort(key=lambda x:x.result)

    context={"team":team,"games":games_final,"news":final_news}
    return render(request, "Darius/team.html", context)

def a_player(request,id):
    context={}
    return render(request, "Darius/player.html", context)