from django.contrib import admin

from .models import News,Tag,Team,Player,RelateNewsTeam,RelateNewsPlayer,SeasonFootball,SeasonBasketball

admin.site.register(News)
admin.site.register(Tag)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(RelateNewsTeam)
admin.site.register(RelateNewsPlayer)
admin.site.register(SeasonFootball)
admin.site.register(SeasonBasketball)