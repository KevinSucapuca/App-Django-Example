from django.http import HttpResponse,request
from django.shortcuts import render,redirect

from django.contrib.auth.mixins import LoginRequiredMixin
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
        return redirect('login')
    

class EpisodeView(LoginRequiredMixin,View):
    def get(self, request, serie_id: int):
        context = {
            'episodes': list(Episodie.objects.filter(serie_id=serie_id))
            

        }
        return render(request, 'episode.html', context=context)
    
    
    




