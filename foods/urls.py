from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

# app_name = "foods"

# router = DefaultRouter()
# router.register("", views.FoodViewSet)
# urlpatterns = router.urls

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
  path('', FoodsView.as_view()),
]