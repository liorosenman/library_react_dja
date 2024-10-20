from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User
from .models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user', 'name', 'city', 'age']

class BookSerializer(serializers.ModelSerializer):            
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'year_published', 'borrow_time', 'filename', 'status']

