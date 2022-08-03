from django.shortcuts import render
from .models import Food
from .serializers import FoodSerializer
from .data.csv_to_db_run import csv_to_db
# for TEST
from rest_framework.viewsets import ModelViewSet


class FoodViewSet(ModelViewSet):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer

def test_csv_to_db(request):
  csv_to_db(Food)
  datas = Food.objects.all()
  ctx = {'datas':datas}
  return render(request, 'templates/test_csv_to_db_view.html', ctx)
  
