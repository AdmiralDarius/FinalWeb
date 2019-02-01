from django.contrib import admin
from games import models


admin.site.register(models.LeagueTeam)
admin.site.register(models.League)
admin.site.register(models.LeagueGame)
admin.site.register(models.Game)
admin.site.register(models.BasketbalState)
admin.site.register(models.FootballState)
admin.site.register(models.Event)
admin.site.register(models.RelateNewsGame)
admin.site.register(models.GamePic)
admin.site.register(models.GameVideo)
admin.site.register(models.PlayersGame)
admin.site.register(models.BasketPlayerGame)
