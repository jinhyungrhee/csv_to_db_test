from rest_framework import serializers
from .models import Post
from foods.models import Food, Category
from foods.serializers import FoodSerializer
from nutrients.serializers import NutrientSerializer
from nutrients.models import Nutrient
from .calculates import calculate
from datetime import date



class PostSerializer(serializers.ModelSerializer):

  # nested serializer 써야할 듯!
  # b_amount = serializers.CharField(default='')
  # l_amount = serializers.CharField(default='')
  # d_amount = serializers.CharField(default='')
  # s_amount = serializers.CharField(default='')

  def get_or_create_foods(self, foods):
      food_ids = []
      for food in foods:
          food_instance, created = Food.objects.get_or_create(pk=food.get('id'), defaults=food)
          food_ids.append(food_instance.pk)
      return food_ids
  
  class Meta:
    model = Post
    # fields = '__all__'
    exclude = ('author',)

  def create(self, validated_data): # post 생성 (이때 음식에 amount 추가 필요)

    breakfast_amount = list(map(float, validated_data['b_amount'][1:-1].split(',')))
    lunch_amount = list(map(float, validated_data['l_amount'][1:-1].split(',')))
    dinner_amount = list(map(float, validated_data['d_amount'][1:-1].split(',')))
    snack_amount = list(map(float, validated_data['s_amount'][1:-1].split(',')))

    result = [0] * 13
    # c_result = set()
    category_result = Category.objects.none() # 빈 쿼리셋 생성
    breakfast = validated_data.pop('breakfast', [])
    # print(breakfast)
    result, category_result = calculate(breakfast, breakfast_amount, result, category_result)

    lunch = validated_data.pop('lunch', [])
    result, category_result = calculate(lunch, lunch_amount, result, category_result)

    dinner = validated_data.pop('dinner', [])
    result, category_result = calculate(dinner, dinner_amount, result, category_result)

    snack = validated_data.pop('snack', [])
    result, category_result = calculate(snack, snack_amount, result, category_result)
    print(result, category_result)
 
    nutrient = Nutrient.objects.create( # 하루 영양정보 생성
      username=validated_data['author'], 
      energy = result[0],
      carbohydrate = result[1],
      protein = result[2],
      fat = result[3],
      dietary_fiber = result[4],
      magnesium = result[5],
      vitamin_a = result[6],
      vitamin_d = result[7],
      vitamin_b6 = result[8],
      vitamin_b12 = result[9],
      folic_acid = result[10],
      tryptophan = result[11],
      dha_epa = result[12],
      created_at = date.today()
    )
    # 오늘 먹은 음식들의 카테고리 기록
    categories_id = []
    for elem in category_result:
      # print(elem[0])
      categories_id.append(elem[0])
    nutrient.category.set(categories_id)

    post = Post.objects.create(**validated_data)
    # print(breakfast[0].id, breakfast[0].energy, breakfast[0].created_at) # 출력 테스트
    post.breakfast.set(breakfast)
    post.lunch.set(lunch)
    post.dinner.set(dinner)
    post.snack.set(snack)
    # print(post)
    return post

