from django.shortcuts import render
from django.http import HttpResponse,request

from django.views.generic.base import View

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
