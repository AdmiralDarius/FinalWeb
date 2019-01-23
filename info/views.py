from django.shortcuts import render

from .models import News

def show_news_list(request):
    context={"news_list":News.objects.all()[0:10],"football_list":News.objects.filter(isfootball=True)[0:10],
             "basketball_list": News.objects.filter(isfootball=False)[0:10] }
    return render(request,"Darius/news.html",context)