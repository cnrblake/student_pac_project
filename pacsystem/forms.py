from django import forms
from .models import StudentTable

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentTable
        fields = ['PacID', 'FirstName', 'LastName', 'Email', 'Course', 'DOB']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
        }