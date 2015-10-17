from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mjCRM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^barcodetest$', 'barcode.views.barcodetest', name='barcodetest'),


    #Receive
    url(r'^rejectionlist/$', 'receive.views.rejectionlist', name='rejectionlist'),
    url(r'^rejectionform/$', 'receive.views.rejectionform', name='rejectionform'),
)