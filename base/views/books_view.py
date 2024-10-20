from rest_framework.permissions import IsAuthenticated
from base.models import Book
from base.serializers import BookSerializer
from rest_framework import status, viewsets
# from customer_views import MyTokenObtainPairSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

