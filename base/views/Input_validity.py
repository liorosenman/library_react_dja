from rest_framework.response import Response
from django.contrib.auth.models import User
import re

def validate_registration(register):
    def wrapper(request, *args, **kwargs):
        data = request.data
        errors = []
        
        # Validating username
        if not data.get('username') or User.objects.filter(username=data['username']).exists():
            errors.append('Username is required and must be unique.')

        # Validating password
        password = data.get('password', '')
        if len(password) < 6 or len(password) > 12 or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append('Password must be between 6 and 12 characters and contain at least one special character.')

        #Validating name
        name = data.get('name', '')
        if len(name) <= 4 or not name.isalpha():
            errors.append('Name must be longer than 4 characters and only contain letters.')
        
        #Validating city
        city = data.get('city', '')
        if not city.isalpha():
            errors.append('City can only contain letters.')
        
        #Validating age
        age = data.get('age', '')
        if not age.isdigit():
            errors.append('Age must be a number.')
        
        # If there are errors, return them all at once
        if errors:
            return Response({'errors': errors}, status=400)
        
        return register(request, *args, **kwargs)
    
    return wrapper
