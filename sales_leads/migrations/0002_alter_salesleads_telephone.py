# Generated by Django 5.0.4 on 2024-04-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesleads',
            name='telephone',
            field=models.CharField(max_length=200),
        ),
    ]