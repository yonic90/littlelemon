# Generated by Django 4.1.5 on 2023-06-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_delete_menuitem_alter_booking_bookingdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateField(db_index=True),
        ),
    ]