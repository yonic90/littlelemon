from django.test import TestCase, Client
from .models import Menu, Booking

from restaurant.serializers import MenuSerializer
from django.urls import reverse

# Create your tests here.
class MenuTest(TestCase):                                                       
    def test_create_item(self):
        item = Menu.objects.create(
            title='IceCream',
            price=80,
            inventory=100)
        
        self.assertEqual(item.title, 'IceCream')
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
        
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        item1= Menu.objects.create(title="chips", price=29, inventory=15)
        item2=Menu.objects.create(title='hamburger', price=44, inventory=6)
        item3 = Menu.objects.create(title='pasta', price=16, inventory=11)

    def test_getall(self):
        menu = Menu.objects.all()
        response = self.client.get(reverse('menu'))
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)        