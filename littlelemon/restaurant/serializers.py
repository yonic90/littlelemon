from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking, MenuItem

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__' 
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['url','username','email','groups'] 
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'                      