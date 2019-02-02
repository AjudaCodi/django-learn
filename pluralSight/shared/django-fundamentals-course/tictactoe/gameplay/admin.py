from django.contrib import admin

# Register your models here.
from .models import Game, Move

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)

admin.site.register(Move)

## shell
# Game.objects.filter(second_player__username="victoria")
# g=Game.objects.get(pk=1)
# g.move_set.all()

## Related m with g
# m.game = g
#  or
# g.move_set.add(m)
