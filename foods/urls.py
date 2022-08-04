from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

app_name = "foods"

router = DefaultRouter()
router.register("", views.FoodViewSet)
urlpatterns = router.urls