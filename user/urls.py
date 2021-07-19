from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.my_profile, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_func, name='logout'),
    path('login/', views.login_, name='login'),
    path('update/', views.user_update, name='user_update'),
    path('user-order/', views.user_orders, name='user-orders'),
    path('user-order-delete/<int:pk>/', views.user_orders_delete, name='user-order-delete'),
    path('orderdetail/<int:pk>', views.user_order_detail, name='user-orderdetail'),
]
