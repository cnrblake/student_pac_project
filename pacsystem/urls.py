from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_student/', view=views.add_student_view, name='add_student'),
    path('add_PAC/', view=views.add_pac_view, name='add_pac'),
    path('pac_list/', view=views.pac_view, name='pac_view'),
]