from rest_framework import serializers
from .models import Progs, Review, Users


class ProgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progs
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
