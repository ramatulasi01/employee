from django.db import models

# Create your models here.
class Employee(models.Model):
    roll no=models1.CharField(max_length=2,blank=True)
    name=models1.CharField(max_length=100)
    phone_number=models1.CharField(max_length=10,blank=True)
         
    
    
    def __str__(self):
          return self.roll no