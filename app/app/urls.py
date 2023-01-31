"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from series.views import SeriesView,EpisodeView
from users.views import LoginView,LogoutView
from series.api.router import router
from rest_framework.documentation import include_docs_urls




urlpatterns = [
    path('admin/', admin.site.urls),
    path('series/', SeriesView.as_view()),
    path('episodes/<int:serie_id>',  EpisodeView.as_view(), name='nameurl'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('docs/', include_docs_urls(title='Mi API Title' , public=False)),
    path('api/',include(router.urls))
    
]
