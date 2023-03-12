"""master URL Configuration

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
from django.urls import include,path
from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('home/',views.index),
    path('home/search/',views.search,name='search'),
    # path('search/',views.input,name='input'),
    path('home/search/external/',views.external),
    path('home/chart/',views.chart,name='chart'),
    path('home/about/',views.about,name='about'),
    path('home/help/',views.help,name='help'),
    path('home/status/',views.status,name='status'),
    path('home/live/',views.live,name='live'),
    path('home/',views.home,name='home'),
    path('home/live/t_status/',views.t_status),
    path('home/status/pnr/',views.pnr),
]
