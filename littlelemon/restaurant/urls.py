from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
#from .views import menuview, bookingview
from .views import MenuItemView, SingleMenuItemView, SingleItemView, msg

urlpatterns = [
    # path('', views.index, name='index'),
    # path('menu/', menuview.as_view()),
    # path('booking/', bookingview.as_view()),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleItemView.as_view()),
    path('message/', views.msg, name="message"),
    
]
