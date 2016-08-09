from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.url_list, name='url_list'),
	url(r'^new/$', views.url_add, name='url_new'),
	url(r'^detail/(?P<url_pk>[0-9]+)/$', views.url_detail, name='url_detail'),
	url(r'^(?P<url_pk>[0-9]+)/delete/$', views.url_delete, name='url_delete'),
]
