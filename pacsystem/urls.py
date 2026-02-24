from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('add_student/', view=views.add_student_view, name='add_student'),
    path('add_PAC/', view=views.add_pac_view, name='add_pac'),
    path('pac_list/', view=views.pac_view, name='pac_view'),
    path('student_list/', view=views.student_view, name='student_view'),
    path('edit_student/<int:f_oid>/', view=views.updateStudent, name='edit_student'),
    path('delete_student/<int:f_oid>/', view=views.deleteStudent, name='delete_student'),
    path('edit_pac/<int:f_oid>/', view=views.updatePAC, name='edit_pac'),
    path('delete_pac/<int:f_oid>/', view=views.deletePAC, name='delete_pac'),

]