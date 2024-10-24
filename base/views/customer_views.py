from django.db import connection
from django.shortcuts import render
from base.models import Customer
from base.serializers import CustomerSerializer
from ..models import User, Customer
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .Input_validity import validate_registration
from django.urls import path
import psycopg2

connection = psycopg2.connect(
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432",
    database="library"
)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @validate_registration
    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
                user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
                user.is_active = True
                user.is_staff = False
                user.save()
                name = request.data['name']
                city = request.data['city'] 
                age = request.data['age'] 
                customer = Customer.objects.create(user=user,name=name,city=city,age=age)
                customer.save()
                return Response({"message": "Customer registered successfully."}, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.get_all_customers()")
                rows = cursor.fetchall() 
                columns = [col[0] for col in cursor.description]
                users = [dict(zip(columns, row)) for row in rows]
            cursor.close()
            connection.close()
            return Response(users, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['id'] = user.id
        token['is_superuser'] = user.is_superuser
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def logout_user(request):
    try:
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "User logged out successfully and token blacklisted."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

