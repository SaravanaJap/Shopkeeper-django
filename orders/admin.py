from django.contrib import admin
from .models import OrderProduct,Orders,Payment

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment','user','product','quantity','ordered')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number','first_name','phone','email','city','order_total','tax','status','is_ordered','created_at']
    list_filter = ['status','is_ordered']
    search_fields = ['order_number','first_name','last_name','phone','email']
    list_per_page = 20
    inlines  = [OrderProductInline]

admin.site.register(Orders,OrderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Payment)



# Register your models here.
