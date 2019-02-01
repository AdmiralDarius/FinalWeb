from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from info.models import Player, Team, News
from sfuser.models import FavouritePlayer, FavouriteTeam, SFComment


def sfuser_player(request,id):
    now=FavouritePlayer.objects.create(user=request.user,player=Player.objects.get(id=id))
    now.save()
    return redirect("/info/a_player/{}".format(id))

def user_register(request):
    if request.POST:
        user = User.objects.create_user(username=request.POST["username"],
                                        email=request.POST["email"],
                                        password=request.POST["password"],
                                        )
        user.save()
    return redirect("/")

def darius_login(request):
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    if user is not None:

        login(request, user)
        return redirect("/")
    else:
        return render(request, "error.html", {'msg':'اطلاعات وارد شده صحیح نیست'})

def darius_logout(request):
    logout(request)
    return redirect("/")

def sfuser_team(request,id):
    now = FavouriteTeam.objects.create(user=request.user, team=Team.objects.get(id=id))
    now.save()
    return redirect("/info/a_team/{}/date".format(id))

def save_comment(request,id):
    now=News.objects.get(id=id)
    another=SFComment.objects.create(news=now,name=request.POST['dame'],text=request.POST['dext'])
    another.save()
    return redirect("/info/news/{}".format(id))