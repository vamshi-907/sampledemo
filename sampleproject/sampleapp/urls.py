from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_student/',views.addstudent,name='add_student'),
]