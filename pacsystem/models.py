from django.db import models

# Create your models here.
class PacTable(models.Model):
    PacID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Department = models.CharField(max_length=255)

    def __str__(self):
        return (f"PAC ID: {self.PacID}\n",
                f"First Name: {self.FirstName}\n"
                f"Last Name: {self.LastName}\n"
                f"Email: {self.Email}\n",
                f"Department: {self.Department}")