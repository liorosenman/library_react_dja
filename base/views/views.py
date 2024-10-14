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
from .Input_validity  import validate_registration

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    
    # @validate_registration
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
