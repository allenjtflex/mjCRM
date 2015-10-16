from django.contrib import admin

# Register your models here.
from .models import Customer, Effective, Person,Catcode


class CustomerAdmin(admin.ModelAdmin):
	list_display=('cust_num', 'title', 'sales', 'is_active')
	search_fields = ['cust_num','title']
	ordering =['cust_num']
	list_filter =('sales', 'is_active',)

class CatcodeAdmin(admin.ModelAdmin):
	list_display=('scode', 'tcode', 'icode', 'describtion')
	list_filter =('scode', 'tcode','is_embedded',)
	ordering =['scode', 'tcode', 'icode',]



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Effective)
admin.site.register(Person)
admin.site.register(Catcode,CatcodeAdmin)