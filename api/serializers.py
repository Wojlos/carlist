from django.db.models import Avg
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api.models import Car, Rating
import requests, json

class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Car

    def get_avg_rating(self, instance):
        avg = Rating.objects.filter(car_id = instance).aggregate(Avg("rating"))
        return avg["rating__avg"]

    def validate(self, data):
        
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{data["make"]}?format=json'

        response = requests.get(url)
        cars = json.loads(response.text)
        
        for car in cars['Results']:
            if car['Model_Name'].lower() == data['model'].lower():
                return data
        raise ValidationError('This car does not exist!')


class PopularCarSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField(read_only = True)

    class Meta:
        model = Car
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    car_id = serializers.PrimaryKeyRelatedField(queryset = Car.objects)
    class Meta:
        fields = ('car_id', 'rating')
        model = Rating
