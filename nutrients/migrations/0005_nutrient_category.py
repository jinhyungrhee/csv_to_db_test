# Generated by Django 4.0.6 on 2022-08-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrients', '0004_remove_nutrient_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrient',
            name='category',
            field=models.CharField(default='미분류', max_length=30),
            preserve_default=False,
        ),
    ]
