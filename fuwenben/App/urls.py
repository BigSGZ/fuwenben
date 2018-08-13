# encoding: utf-8
from django.conf.urls import url

from App import views




urlpatterns=[
    url(r'^hello/',views.hello,name='hello'),
    url(r'^suggest/',views.suggest,name='suggest')
]
