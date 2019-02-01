from django.contrib import admin

from .models import FavouriteGame,FavouriteTeam,FavouritePlayer,SFComment

admin.site.register(FavouriteGame)
admin.site.register(FavouritePlayer)
admin.site.register(FavouriteTeam)
admin.site.register(SFComment)