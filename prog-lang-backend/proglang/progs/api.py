from .models import Progs, Review, Users
from rest_framework import viewsets, permissions
from .serializers import ProgSerializer, ReviewSerializer, UserSerializer

class ProgViewSet(viewsets.ModelViewSet):
    queryset = Progs.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProgSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer