from django.shortcuts import render
from django.http import HttpResponse,request
from django.contrib.auth import authenticate, login
from django.views.generic.base import View

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse(content= b'Success')
        return self.get(request)