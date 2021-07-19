from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('addtoshopcart/<int:pk>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:pk>', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
    path('shopcart/', views.shopcart, name='shopcart'),
]
