from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'build', views.build),
    url(r'select/$', views.select),
    url(r'select/force/$',views.select, {'force': '1'}),
]
