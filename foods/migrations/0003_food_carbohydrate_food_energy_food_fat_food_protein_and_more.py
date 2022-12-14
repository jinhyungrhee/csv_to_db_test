# Generated by Django 4.0.6 on 2022-08-02 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_category_options_food_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='carbohydrate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='food',
            name='energy',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='food',
            name='fat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='food',
            name='protein',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='dha_epa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='dietary_fiber',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='folic_acid',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='magnesium',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='tryptophan',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamin_b12',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamin_b6',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamin_c',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='food',
            name='vitamin_d',
            field=models.FloatField(default=0.0),
        ),
    ]
