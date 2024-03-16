from django.contrib import admin
from django.urls import path , include
from.import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('search/',views.search,name="search"),
    path('search/res/',views.searchres,name="searchres"),
    path('search/res/book',views.book,name="book"),
    path('chart/',views.chart,name="chart"),
    path('chart/get',views.getchart,name="getchart"),
    path('live/',views.live,name="live"),
    path('live/status',views.status,name="status"),
    path('enquiry/',views.enquiry,name="enquiry"),
    path('enquiry/get',views.getPNR,name="getPNR"),
    path('help/',views.home,name="help"),
    path('about/',views.home,name="about"),
    path('improutes/',views.home,name="improutes"),
    path('data/', views.DataAPI.as_view(), name='api'),

]