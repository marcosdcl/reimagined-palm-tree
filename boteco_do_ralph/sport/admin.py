from sport.models import Sport
from django.contrib import admin


class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Sport, SportAdmin)
