from django.http import HttpResponse,request
from django.shortcuts import render


# Create your views here.
from django.views.generic.base import View


class HelloWorld(View):

    
    def get(self, request):
        context ={
            'items':list(range(10))
            
        }
        return render(request, 'index.html' , context = context)



