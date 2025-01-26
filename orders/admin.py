from django.contrib import admin
from .models import OrderProduct,Orders,Payment

admin.site.register(Orders)
admin.site.register(OrderProduct)
admin.site.register(Payment)

# Register your models here.
