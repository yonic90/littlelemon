from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255, db_index=True, null=False, blank=False)
    Price = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
    Inventory = models.SmallIntegerField(default=0, null=False, blank=False)
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class Booking(models.Model):
    Name = models.CharField(max_length=255, db_index=True, null=False, blank=False)
    No_of_guests= models.SmallIntegerField(null=False, blank=False)
    BookingDate = models.DateField(db_index=True, null=False, blank=False)
    
    def __str__(self):
        return f"{self.Name} for date: {str(self.BookingDate)}"  


  
