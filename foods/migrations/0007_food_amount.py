# Generated by Django 4.0.6 on 2022-08-03 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_alter_food_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
