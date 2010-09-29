from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'imghost.views.index'),
    (r'^(?P<picture_id>\d+)/$', 'imghost.views.picture_detail'),
    (r'^upload/$', 'imghost.views.upload'),
    (r'^esam/(?P<path>.*)' , 'django.views.static.serve',{'document_root': 'esam'}),

)

