from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('volunteer', views.volunteer, name='volunteer'),
    path('student', views.student, name='student'),
    path('student_reg_2', views.student_reg_2, name='student_reg_2'),
    path('', views.index, name='index'),
    path('volunteer_reg', views.volunteer_registration, name='volunteer_reg')
]
