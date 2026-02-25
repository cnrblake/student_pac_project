from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_student/', view=views.add_student_view, name='add_student'),
    path('add_PAC/', view=views.add_pac_view, name='add_pac'),
    path('pac_list/', view=views.pac_view, name='pac_view'),
    path('student_list/', view=views.student_view, name='student_view'),
    path('edit_student/<int:f_oid>/', view=views.update_student, name='edit_student'),
    path('delete_student/<int:f_oid>/', view=views.delete_student, name='delete_student'),
    path('edit_pac/<int:f_oid>/', view=views.update_PAC, name='edit_pac'),
    path('delete_pac/<int:f_oid>/', view=views.delete_PAC, name='delete_pac'),
    path('pac_students/', view=views.assigned_students_to_Pac, name='pac_students'),

]