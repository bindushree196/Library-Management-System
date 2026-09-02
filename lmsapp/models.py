from django.db import models

class Library(models.Model):
    Student_Name = models.CharField(max_length=50)
    Title = models.CharField()
    Quantity = models.IntegerField()
    Author = models.CharField(max_length=100)
    ISBN= models.IntegerField()
    Published_Date= models.DateField()

def __str__(self):
    return self.Name
