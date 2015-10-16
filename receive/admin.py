from django.contrib import admin

# Register your models here.
from .models import Rejection
from .forms import RejectionForm


class RejectionAdmin(admin.ModelAdmin):

	list_display=['deliver_at' ,'cctno','customer','deliver','quantity','uom']
	form = RejectionForm

	fieldsets = [        
        ('Deliver', {'fields': ['deliver_at','deliver','deliver_num']}),
        ('Customer', {'fields': ['customer','cctno']}),
        ('Quantity information', {'fields': ['quantity','uom',]}),
        (None, {'fields': ['wmemo']}),
    ]




admin.site.register(Rejection,RejectionAdmin)
