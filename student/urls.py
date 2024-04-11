from django.contrib import admin
from django.urls import path, include
from student import views

urlpatterns = [
    path('insertStudent/', views.insertStudent, name='insertStudent'),
    path('singleRow/<int:student_id>/', views.singleRow, name='singleRow'),
]