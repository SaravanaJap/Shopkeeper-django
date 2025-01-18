from django.shortcuts import render
from store.models import Product
from carts.views import CartItem

# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available = True)
    count = CartItem.objects.count()
    context = {
        'products':products,
        'count':count
    }
    return render(request,"shop/home.html",context)
