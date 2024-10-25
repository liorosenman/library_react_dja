from django import views
from django.contrib import admin
from django.urls import include, path
from base.views.books_view import BookViewSet
from base.views.customer_views import CustomerViewSet, logout_user, show_all_customers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView


router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    
    path('logout/', logout_user, name='logout'),
    path('list_all_customers/', show_all_customers, name="showall")
]
