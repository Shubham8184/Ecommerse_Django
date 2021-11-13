from django.contrib import admin
from .models import Order_item,Custorders


class OrderitemsAdmin(admin.ModelAdmin):
    list_display=['id','customer','laptop','mobile','grocery','price','quantity']
admin.site.register(Order_item,OrderitemsAdmin)

class CustOrderitemsAdmin(admin.ModelAdmin):
    list_display=['id','date','customer','laptop','mobile','grocery','price','items','address','fname','lname','mobile_no']
admin.site.register(Custorders,CustOrderitemsAdmin)



