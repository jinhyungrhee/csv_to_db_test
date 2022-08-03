import csv
import os, sys
import django

def csv_to_db(django_model):
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
  django.setup()
  csv_path = '/config/foods/data/csv_to_db.csv'
  with open(csv_path, newline='') as f_csv:
    row_dics = csv.DictReader(f_csv)
    for row in row_dics:
      print(row)
      django_model.objects.create(
        id = row['id'],
        name = row['name'],
        category_id = row['category_id'],
        energy = row['energy'],
        protein = row['protein'],
        fat = row['fat'],
        carbohydrate = row['carbohydrate'],
        dietary_fiber = row['dietary_fiber'],
        magnesium = row['magnesium'],
        vitamin_a = row['vitamin_a'],
        vitamin_d = row['vitamin_d'],
        vitamin_b6 = row['vitamin_b6'],
        folic_acid = row['folic_acid'],
        vitamin_b12 = row['vitamin_b12'],
        tryptophan = row['tryptophan'],
        dha_epa = row['dha_epa']
      )