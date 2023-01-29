from django.http import HttpResponse,request
from django.shortcuts import render


# Create your views here.
from django.views.generic.base import View


class HelloWorld(View):

    
    def get(self, request):
        return HttpResponse(content = b'Hello World')
