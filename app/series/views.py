from django.http import HttpResponse,request
from django.shortcuts import render


# Create your views here.
from django.views.generic.base import View

from series.models import Serie

class SeriesView(View):
    def get(self, request):
        context = {
            'series' : list(Serie.objects.all())

        }
        return render(request, 'series.html', context)




