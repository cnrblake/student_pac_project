from django.db import models

# initialization of the PAC and Student table
class PacTable(models.Model):
    PacID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=64, null=False)
    LastName = models.CharField(max_length=64, null=False)
    Email = models.EmailField(max_length=255, null=False)
    Department = models.CharField(max_length=64, null=False)

    # allows the contents of the PAC table to be shown
    def __str__(self):
        return f"PAC {self.PacID}: {self.FirstName} {self.LastName} ({self.Email}) - {self.Department}"
    
class StudentTable(models.Model):
    StudentID = models.AutoField(primary_key=True)
    PacID = models.ForeignKey(PacTable, on_delete=models.CASCADE, null=True, blank=True)

    FirstName = models.CharField(max_length=64, null=False)
    LastName = models.CharField(max_length=64, null=False)

    Email = models.EmailField(max_length=255, null=False)
    Course = models.CharField(max_length=64, null=False)
    DOB = models.DateField(null=False)

    # allows the contents of the student table to be shown
    def __str__(self):
        return f"Student {self.StudentID}: {self.FirstName} {self.LastName} PAC ID: {self.PacID} ({self.Email}) - {self.Course} - {self.DOB}"