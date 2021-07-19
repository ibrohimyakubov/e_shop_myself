from django.urls import path
from basic import views

app_name = 'basic'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>/', views.category_products, name='category_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
