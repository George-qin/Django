from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^text/$',views.index),
    url(r'^register/$',views.register),
    url(r'^person/$',views.person),
    url(r'^weather/$', views.weather),
    url(r'^LiuYan/$', views.liulan),
    url(r'^check/$', views.check),
]