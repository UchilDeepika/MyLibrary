from django.db import models

# Create your models here.
class Book(models.Model):   
    name= models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=25)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    available=models.BooleanField(default=True)


class Author(models.Model):
    fisrtname=models.CharField(max_length=100)  
    lastname=models.CharField(max_length=100) 
    category=models.CharField(max_length=25)
    info=models.CharField(max_length=100) 


class Categories(models.Model):
    category=models.CharField(max_length=25)      