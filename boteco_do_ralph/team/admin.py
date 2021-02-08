from team.models import Team
from django.contrib import admin


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Team, TeamAdmin)
