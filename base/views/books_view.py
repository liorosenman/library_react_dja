from django.db import connection
from rest_framework.permissions import IsAuthenticated
from base.models import Book
from base.serializers import BookSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from base.utils import extract_parameters_from_request


# from customer_views import MyTokenObtainPairSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "You are not authorized to add books."}, status=status.HTTP_403_FORBIDDEN)
        proc_name = 'add_book'
        print(request.data.get('borrow_time'))
        name = request.data.get('name')
        author = request.data.get('author')
        year_published = request.data.get('year_published')
        borrow_time = request.data.get('borrow_time')
        filename = request.data.get('filename')
        status_value = request.data.get('status')
        # param_list = list(parameters.values())
        print(name)
        try:
            with connection.cursor() as cursor:
            #     cursor.callproc('add_book', [
            #         name, 
            #         author, 
            #         year_published, 
            #         borrow_time, 
            #         filename, 
            #         status_value
            #     ])
                # cursor.execute("CALL add_book('expbook', 'noauthor', 2024, 5, 'pic2.png', 'available');")
                # cursor.callproc(proc_name,[name, author, year_published, borrow_time, filename, status_value])
                print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
                cursor.execute("CALL add_book(%s, %s, %s, %s, %s, %s);", [name, author, year_published, borrow_time, filename, status_value])
            return Response({'message': 'Book added successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        




    


