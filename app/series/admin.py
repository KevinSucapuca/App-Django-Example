from django.contrib import admin

# Register your models here.


from django.contrib.admin import ModelAdmin, register
from series.models import Serie,Episodie


class SeriesAdmin(ModelAdmin):
    pass

admin.site.register(Serie, SeriesAdmin)


@register(Episodie)
class EpisodieAdmin(ModelAdmin):
    pass
