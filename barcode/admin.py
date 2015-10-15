from django.contrib import admin

# Register your models here.
from .models import Barcode


class BarcodeAdmin(admin.ModelAdmin):
	list_display=('bformat', 'barcodelen', 'regexpstring')


admin.site.register(Barcode, BarcodeAdmin)



