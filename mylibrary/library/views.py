from django.shortcuts import render
from .models import Book

# Create your views here.
def StudentHomePage(request):   
    books=Book.objects.all()
    return render(request,'StudentsHomePage.html', {'books':books})