# Generated by Django 5.0.4 on 2024-04-10 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loancalculator',
            name='down_payment',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='loancalculator',
            name='interest_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='loancalculator',
            name='loan_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='loancalculator',
            name='num_of_months',
            field=models.FloatField(default=0),
        ),
    ]
