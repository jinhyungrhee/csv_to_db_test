# Generated by Django 4.0.6 on 2022-08-03 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_remove_food_amount_remove_food_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ManyToManyField(blank=True, to='foods.category'),
        ),
    ]
