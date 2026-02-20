from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentTable
        fields = ['PacID', 'FirstName', 'LastName', 'Email', 'Course', 'DOB']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
        }

class PacForm(forms.ModelForm):
    class Meta:
        model = models.PacTable
        fields = ['FirstName', 'LastName', 'Email', 'Department']
        