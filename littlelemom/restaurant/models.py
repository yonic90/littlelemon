from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests= models.IntegerField(max_length=6)
    BookingDate = models.DateField(auto_now_add=True)

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=2, max_length=10)
    Inventory = models.IntegerField(max_length=5)
