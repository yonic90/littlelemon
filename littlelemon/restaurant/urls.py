from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
# from . import views
#from .views import menuview, bookingview
from .views import MenuItemsView, SingleMenuItemView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('menu/', menuview.as_view()),
    # path('booking/', bookingview.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    
]
