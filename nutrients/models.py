from django.db import models
from django.contrib.auth.models import User
from foods.models import Category

class Nutrient(models.Model):
  username = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

  energy = models.FloatField(default=0.0)
  carbohydrate = models.FloatField(default=0.0)
  protein = models.FloatField(default=0.0)
  fat = models.FloatField(default=0.0)

  dietary_fiber = models.FloatField(default=0.0)
  magnesium = models.FloatField(default=0.0)
  vitamin_a = models.FloatField(default=0.0)
  vitamin_d = models.FloatField(default=0.0)
  vitamin_b6 = models.FloatField(default=0.0)
  vitamin_b12 = models.FloatField(default=0.0)
  folic_acid = models.FloatField(default=0.0)
  tryptophan = models.FloatField(default=0.0)
  dha_epa = models.FloatField(default=0.0)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  category = models.ManyToManyField(Category, blank=True) # 수정 필요
  # category = models.CharField(max_length=30) # 만약 리스트로 받아야 한다면? ForeignKey나 ManyToManyField 사용

  def __str__(self):
    return f'[{self.username}\'의 오늘하루 영양성분표 :: {self.created_at}]'
    