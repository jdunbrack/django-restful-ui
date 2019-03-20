from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<show_id>\d+)$', views.show_details),
    url(r'(?P<show_id>\d+)/edit$', views.show_edit),
    url(r'(?P<show_id>\d+)/destroy$', views.show_delete),
    url(r'new$', views.show_new),
    url(r'title-check$', views.verify_title),
    url(r'edit-title-check$', views.verify_edit_title)
]