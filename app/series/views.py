from django.http import HttpResponse,request,Http404
from django.shortcuts import render


# Create your views here.
from django.views.generic.base import View

from series.models import Serie,Episodie

class SeriesView(View):
    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'series' : list(Serie.objects.all())

            }
            return render(request, 'series.html', context=context)
        return Http404()
    

class EpisodeView(View):
    def get(self, request, serie_id: int):
        context = {
            'episodes': list(Episodie.objects.filter(serie_id=serie_id))
            

        }
        return render(request, 'episode.html', context=context)
    
    
    




