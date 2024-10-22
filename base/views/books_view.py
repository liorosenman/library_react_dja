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

    # def create(self, request, *args, **kwargs):
    #     if not request.user.is_superuser:
    #         return Response({"detail": "You are not authorized to add books."}, status=status.HTTP_403_FORBIDDEN)
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save() 
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "You are not authorized to add books."}, status=status.HTTP_403_FORBIDDEN)
        # parameters = extract_parameters_from_request(request)
        proc_name = 'add_book'
        print(request.data.get('borrow_time'))
        name = request.data.get('name'),
        author = request.data.get('author'),
        year_published = int(request.data.get('year_published')),
        borrow_time = int(request.data.get('borrow_time')),
        filename = request.data.get('filename'),
        status = request.data.get('status')
        # param_list = list(parameters.values())
        try:
            with connection.cursor() as cursor:
                # cursor.callproc(proc_name, param_list)
                cursor.execute("CALL add_book(%s, %s, %s, %s, %s, %s);", (name, author, year_published, borrow_time, filename,status))
            return Response({"detail": "Book added successfully."})
        except Exception as e:
            return Response({"detail": str(e)})



    


