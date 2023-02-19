from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('current',views.current,name="current"),
    path('series',views.series,name="series"),
    path('players',views.players,name="players"),
]