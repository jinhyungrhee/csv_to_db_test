# Generated by Django 4.0.6 on 2022-08-05 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrients', '0002_nutrient_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrient',
            old_name='vitamin_c',
            new_name='vitamin_a',
        ),
    ]
