from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Author, Book, BooksCheckedOut

# Create your views here.


def StudentHomePage(request):
    books = Book.objects.all().filter(available=True)[:3]
    bookscheckedout = BooksCheckedOut.objects.filter(
        username=request.user.username, returned=False).select_related("bookid")
    return render(request, 'StudentsHomePage.html', {'books': books, 'bookscheckedout': bookscheckedout})


def BookDetails(request):
    if request.method == "POST":
        bookname = request.POST['bookname']
        book = Book.objects.all().filter(name=bookname)
        return render(request, 'BookDetails.html', {'book': book})


def CheckOut(request):
    if request.method == "POST":
        bookname = request.POST['book_name']
        checkout = BooksCheckedOut()
        checkout.bookid = Book.objects.get(name=bookname)
        checkout.username = request.user.username
        checkout.checkedoutdate = timezone.now()
        checkout.save()
        book = Book.objects.get(name=bookname)
        book.available = False
        book.save(update_fields=['available'])
        return redirect('StudentHomePage')


def index(request):
    books = Book.objects.all().filter(available=True).select_related("author")
    return render(request, 'index.html', {'books': books})


def returnbook(request):
    if request.method == "POST":
        bookname = request.POST['book_name']
        bookid = Book.objects.get(name=bookname)
        bookid.available = True
        bookid.save(update_fields=['available'])
        checkout = BooksCheckedOut.objects.get(bookid_id=bookid)
        checkout.returned = True
        checkout.save(update_fields=['returned'])
        return redirect('StudentHomePage')
