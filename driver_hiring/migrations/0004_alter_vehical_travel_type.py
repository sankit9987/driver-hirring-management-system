# Generated by Django 4.0.2 on 2022-03-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_hiring', '0003_contact_us_vehical_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehical',
            name='travel_type',
            field=models.CharField(choices=[('incity', 'incity'), ('outstation', 'outstation')], max_length=100),
        ),
    ]