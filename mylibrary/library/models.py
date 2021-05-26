from django.db import models
from django.utils import timezone



class Categories(models.Model):
    category=models.CharField(max_length=25)      


class Author(models.Model):
    fisrtname=models.CharField(max_length=100)  
    lastname=models.CharField(max_length=100) 
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    info=models.CharField(max_length=100) 

# Create your models here.
class Book(models.Model):   
    name= models.CharField(max_length=100)
    author= models.ForeignKey(Author, on_delete=models.CASCADE)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    available=models.BooleanField(default=True)


class BooksCheckedOut(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)   
    username=models.CharField(max_length=100)
    checkedoutdate=models.DateField(default=timezone.now)
    returned = models.BooleanField(default=False)