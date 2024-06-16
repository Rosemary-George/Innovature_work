from django.urls import path
from . import views
from .views import ProductListCreate, ProductDetail

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    
]

