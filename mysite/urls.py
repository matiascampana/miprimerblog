from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #Examples:
    #url(r'^$', 'mysite.views.home', name='home'),


    url(r'^admin/', admin.site.urls name='admin'),
    url(r'^blog/', blog.urls name='blog'),

]
