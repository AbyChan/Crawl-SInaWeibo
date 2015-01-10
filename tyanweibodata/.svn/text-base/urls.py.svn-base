from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^fetch/$','fetchweibodata.views.control'),
    (r'^fetch/start/$','fetchweibodata.views.startfetchtofile'),
    (r'^fetch/test/$','fetchweibodata.views.test'),
    (r'^fetch/testmail/$','fetchweibodata.views.mailtest'),
    # Examples:
    # url(r'^tyanweibodata/', include('tyanweibodata.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
