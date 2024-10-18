import enum
from django.db import models
from django.contrib.auth.models import User
from enum import Enum

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
    

class BookType(Enum):
    TYPE_1 = 10
    TYPE_2 = 5
    TYPE_3 = 2

BOOK_TYPE_CHOICES = [
    (BookType.TYPE_1.value, 'Type_1'),
    (BookType.TYPE_2.value, 'Type_2'),
    (BookType.TYPE_3.value, 'Type_3'),
]

class BookStatus(enum.Enum):
     AVAILABLE = "available"
     LOANED = "loaned"
     ERASED = "erased"

BOOK_STATUS_CHOICES = [
    (BookStatus.AVAILABLE.value, 'Available'),
    (BookStatus.LOANED.value, 'Loaned'),
    (BookStatus.ERASED.value, 'Erased'),
]

class BookStatus(enum.Enum):
     AVAILABLE = "available"
     LOANED = "loaned"
     ERASED = "erased"

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year_published = models.IntegerField()
    borrow_time = models.IntegerField(choices=BOOK_TYPE_CHOICES, default=BookType.TYPE_1.value)
    filename = models.ImageField(upload_to='book_images/', null=True, blank=True) 
    status = models.CharField(choices=BOOK_STATUS_CHOICES, default=BookStatus.AVAILABLE.value, null=False, max_length=20)

    def __str__(self):
        return self.name

