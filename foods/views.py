from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Food
from .serializers import FoodSerializer
from django.db.models import Q
# for TEST
from rest_framework.viewsets import ModelViewSet


class FoodViewSet(ModelViewSet):
  queryset = Food.objects.all()
  serializer_class = FoodSerializer

  
class FoodsView(APIView):

  def get(self, request):
    paginator =PageNumberPagination()
    paginator.page_size = 10000
    search_query = request.GET.get("search", None)
    print(search_query)
    if search_query != None:
      foods = Food.objects.filter(Q(name__icontains=search_query)).order_by('classifier')
    else:
      foods = Food.objects.all()
    results = paginator.paginate_queryset(foods, request)
    serializer = FoodSerializer(results, many=True)
    return paginator.get_paginated_response(data=serializer.data)