from django.db import models

# Create your models here.
class PacTable(models.Model):
    PacID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255, null=False)
    LastName = models.CharField(max_length=255, null=False)
    Email = models.EmailField(max_length=255, null=False)
    Department = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"PAC {self.PacID}: {self.FirstName} {self.LastName} ({self.Email}) - {self.Department}"
    
class StudentTable(models.Model):
    StudentID = models.AutoField(primary_key=True)
    PacID = models.ForeignKey(PacTable, on_delete=models.CASCADE) # need to fill foreign key in

    FirstName = models.CharField(max_length=255, null=False)
    LastName = models.CharField(max_length=255, null=False)

    Email = models.EmailField(max_length=255, null=False)
    Course = models.CharField(max_length=255, null=False)
    DOB = models.DateField(null=False)

