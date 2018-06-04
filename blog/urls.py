__author__ = 'Pavan Kotehal'

from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.BlogList.as_view(), name='bloglist'),
    url(r'^(?P<pk>\d+)/$', views.BlogDetail.as_view(), name='blogdetail'),
    #url(r'^blogs/all/$', views.BlogViewset.as_view(), name='blogviewset'),
    url(r'^create/$', views.BlogCreate.as_view(), name='blogcreate'),
]