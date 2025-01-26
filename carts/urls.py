from django.urls import path
from .views import *

urlpatterns = [
    path('',cart,name='cart'),
    path('add_cart/<int:product_id>/',add_cart,name='add_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/',remove_cart,name='remove_cart'),
    path('delete_item/<int:product_id>/<int:cart_item_id>/',delete_item,name='delete_item'),
    path('checkout/',checkout,name='checkout'),
    

]


