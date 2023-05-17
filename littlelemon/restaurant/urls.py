from django.contrib import admin
from django.urls import path
# from . import views
from .views import menuview, bookingview

urlpatterns = [
    # path('', views.index, name='index'),
    path('menu/', menuview.as_view()),
    path('booking/', bookingview.as_view()),
    
]
