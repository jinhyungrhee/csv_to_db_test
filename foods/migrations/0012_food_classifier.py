# Generated by Django 4.0.6 on 2022-08-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='classifier',
            field=models.IntegerField(default=0),
        ),
    ]