from django.contrib import admin

# Register your models here.
from .models import Barcode, Definecaption, Encoder


# Custom admin interface
class BarcodeAdmin(admin.ModelAdmin):
	list_display=('bformat', 'barcodelen', 'regexpstring')


class DefinecaptionAdmin(admin.ModelAdmin):
	list_display=('id', 'caption')


class EncoderAdmin(admin.ModelAdmin):
	list_display=('bformat', 'caption', 'start_position', 'char_length')
	list_filter = ('bformat', 'caption',)



# Add model to admin site manage
admin.site.register(Barcode, BarcodeAdmin)
admin.site.register(Definecaption,DefinecaptionAdmin)
admin.site.register(Encoder, EncoderAdmin)



