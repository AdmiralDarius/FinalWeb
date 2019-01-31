from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from sfuser.models import FavouritePlayer, FavouriteTeam, FavouriteGame
from .models import News, RelateNewsTeam, RelateNewsPlayer, Tag, Team, Player
from games.models import RelateNewsGame, Game

from django.utils import timezone
def show_news_list(request):
    pages=8
    if request.POST:
        pages=int(request.POST['choice'])

    news_list=set()
    msg=""
    if request.user.is_authenticated:

        fteam=FavouriteTeam.objects.filter(user=request.user).all()
        fplayer = FavouritePlayer.objects.filter(user=request.user).all()
        fgame = FavouriteGame.objects.filter(user=request.user).all()

        for news in News.objects.all():
            from django.utils import timezone
            result=timezone.now() - news.date_added
            if result.days>2:
                continue
            news.day=result.days
            for team in fteam:
                if RelateNewsTeam.objects.filter(news=news,team=team.team).exists():
                    news_list.add(news)
            for game in fgame:
                if RelateNewsGame.objects.filter(news=news,game=game.game).exists():
                    news_list.add(news)
            for player in fplayer:
                if RelateNewsPlayer.objects.filter(news=news,player=player.player).exists():
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
        tmp_games_list = FavouriteGame.objects.filter(user=request.user) \
            .filter(game__date__lt=timezone.now() + timezone.timedelta(days=1)) \
            .filter(game__date__gt=timezone.now() + timezone.timedelta(days=-1)).all()
        games_list=[]
        for i in tmp_games_list:
            games_list.append(i.game)
    else:
        msg = "لطفا ابتدا وارد سیستم شوید تا مورد علاقه ها نمایش داده شود"
    games_list.reverse()
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

def result_to_str(num):
    if num==0:
        return "مساوی"
    if num>0:
        return "برد"
    return "باخت"

def a_team_sortbythis(request,id,sortbythis):
    team=Team.objects.get(id=id)

    raw_news=News.objects.all()
    final_news=[]
    for now in raw_news:
        dorost=False
        flag=True
        cur_tex=now.body+now.title
        for i in now.tag_set.all():
            cur_tex+=i.description
        if team.name in cur_tex:
            dorost = True
        for i in team.player_set.all():
            if i.name not in cur_tex:
                dorost = True
        if request.POST:
            for i in request.POST['searchby'].split():
                if i not in cur_tex:
                    flag = False
        if flag and dorost:
            final_news.append(now)

    games_final=[]

    raw_games=Game.objects.filter(Q(team1=team)|Q(team2=team)).all()
    for game in raw_games:
        tmp={}
        result_num=0
        if game.is_football:
            result_num=game.football_states.f_score-game.football_states.s_score
        else:
            result_num = game.basketball_states.f_total_score - game.basketball_states.s_total_score
        if game.team1==team:
            tmp['team']=game.team2
            tmp['result']=result_to_str(result_num)
        else:
            tmp['team'] = game.team1
            tmp['result'] = result_to_str(-result_num)

        tmp['date']=game.date
        games_final.append(tmp)

    if sortbythis=='date':
        games_final.sort(key=lambda x:x['date'])
    if sortbythis=='opponent':
        games_final.sort(key=lambda x:x['team'].name)
    if sortbythis=='result':
        games_final.sort(key=lambda x:x['result'])

    sf_is_fav=False
    sf_is_auth=False
    if request.user.is_authenticated:
        sf_is_auth=True
        if FavouriteTeam.objects.filter(user=request.user, team=team).exists():
            sf_is_fav=True
        else:
            sf_is_fav=False
    else:
        sf_is_auth=False

    context={"team":team,"games":games_final,"news":final_news,"sf_is_fav":sf_is_fav,"sf_is_auth":sf_is_auth}
    return render(request, "Darius/team.html", context)

def a_player(request,id):
    player = Player.objects.get(id=id)
    in_news=[]
    search=""
    if request.POST:
        search=request.POST['searchby']
    for i in News.objects.all():
        news_whole=i.title+" "+i.body
        for j in i.tag_set.all():
            news_whole+=" "+j.description
        flag=False
        for j in search.split():
            if not j in news_whole:
                flag=True
        if flag:
            continue
        if player.name not in news_whole:
            continue
        in_news.append(i)
    sf_is_fav=False
    sf_is_auth=False

    if request.user.is_authenticated:
        sf_is_auth=True
        if FavouritePlayer.objects.filter(user=request.user, player=player).exists():
            sf_is_fav=True
        else:
            sf_is_fav=False
    else:
        sf_is_auth=False
    if player.isfootball:
        the_set=player.seasonfootball_set.all()
    else:
        the_set=player.seasonbasketball_set.all()
    in_news.reverse()
    context={"player":player,'sf_is_auth':sf_is_auth,'sf_is_fav':sf_is_fav,"the_set":the_set,"in_news":in_news}
    return render(request, "Darius/player.html", context)

def index(request):
    return redirect("/info/news")