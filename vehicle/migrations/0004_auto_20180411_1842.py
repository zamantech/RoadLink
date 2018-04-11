# Generated by Django 2.0.4 on 2018-04-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20180411_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='booked',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='name',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='cost_per_km',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuel_type',
            field=models.CharField(default='petrol', max_length=200),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='insurance_status',
            field=models.CharField(choices=[('U', 'Updated'), ('NU', 'Not Updated')], default='NU', max_length=2),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='mileage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='no_of_km_travelled',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='owner',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.DecimalField(decimal_places=3, default='0', max_digits=20),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='registration_plate',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_status',
            field=models.CharField(choices=[('B', 'Booked'), ('NB', 'Not Booked')], default='NB', max_length=2),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('P', 'Passenger'), ('T', 'Truck'), ('C', 'Construction')], default='P', max_length=1),
        ),
    ]
