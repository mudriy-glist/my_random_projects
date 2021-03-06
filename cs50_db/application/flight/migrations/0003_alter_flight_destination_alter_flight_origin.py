# Generated by Django 4.0.6 on 2022-07-27 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flight.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flight.airport'),
        ),
    ]
