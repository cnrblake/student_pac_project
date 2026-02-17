from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_student/', view=views.add_student_view, name='add_student'),
]