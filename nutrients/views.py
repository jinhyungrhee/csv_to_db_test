from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Nutrient
from .serializers import NutrientSerializer

# Create your views here.
class NutrientView(APIView):
  def get(self, request):
    try:
      nutrient = Nutrient.objects.filter(username=request.user)
      print(nutrient)
      serializer = NutrientSerializer(nutrient, many=True).data
      return Response(serializer)
    except Nutrient.DoesNotExist: # 수정이 필요할까?
      return Response(status=status.HTTP_404_NOT_FOUND)