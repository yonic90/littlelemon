from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests= models.IntegerField()
    BookingDate = models.DateField(auto_now_add=True)

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField()

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.SmallIntegerField()
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'    
