from django.contrib import admin
from django.urls import path, include, re_path
from mark import views

urlpatterns = [
    path('', views.options, name='options'),
    path('insertMark/', views.insertMark, name='insertMark'),
    path('displayRecord/', views.displayRecord, name='displayRecord'),
    path('oneRow/', views.oneRow, name='oneRow'),
    re_path(r'^updateMark/(?P<pk>\d+)/$', views.updateMark, name='updateMark'),
    re_path(r'^delectRow/(?P<pk>\d+)/$', views.delectRow, name='delectRow')
    
]