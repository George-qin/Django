from .import views
from  django.conf.urls import url
urlpatterns=[
    url(r'^$',views.index),
    url('^person/$',views.Person),
    url(r'^skill/$',views.Skill),
    url(r'^person/(\d+)$',views.ShowPersonSkill),
    url(r'^main/$',views.main),
    url(r'^main/login$',views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$',views.quit),
    url(r'^register/$',views.register),
    url(r'^okregister/$',views.okregister),
    url(r'^judge/$', views.judge),
    url(r'^main/text$', views.text,name='text'),
]