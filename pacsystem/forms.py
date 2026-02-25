from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        # the table that is used within this form
        model = models.StudentTable
        # what fields to display to the user and can be modified by the user
        fields = ['PacID', 'FirstName', 'LastName', 'Email', 'Course', 'DOB']
        # any widgets that are required for easier date inputting, here a date input.
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
        }

class PacForm(forms.ModelForm):
    class Meta:
        model = models.PacTable
        fields = ['FirstName', 'LastName', 'Email', 'Department']
        