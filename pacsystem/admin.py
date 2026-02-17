from django.contrib import admin
from . models import PacTable
from . models import StudentTable

# Register your models here.
admin.site.register(PacTable)
admin.site.register(StudentTable)