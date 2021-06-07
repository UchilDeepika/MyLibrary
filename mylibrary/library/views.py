from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib import messages

from .models import Book, BooksCheckedOut, Author


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
        number = BooksCheckedOut.objects.filter(username=request.user.username, returned=False).count()
        print(number)
        if number == 3:
            messages.info(request, "You can only have 3 books at a time!")
            return render(request, 'BookDetails.html')
        else:
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


def BooksSearch(request):
    if 'term' in request.GET:
        qs = Book.objects.filter(name__istartswith=request.GET.get('term'))
        books = list()
        for book in qs:
            books.append(book.name)
        return JsonResponse(books, safe=False)
    return render(request, 'BrowseBooks.html')


def AuthorSearch(request):
    if 'term' in request.GET:
        qs = Author.objects.filter(fisrtname__istartswith=request.GET.get('term'))
        authors = list()
        for author in qs:
            authors.append(author.fisrtname + " " + author.lastname)
        return JsonResponse(authors, safe=False)
    return render(request, 'BrowseBooks.html')


def BrowseBooks(request):
    return render(request, 'BrowseBooks.html')


def SearchedBooks(request):
    if request.method == "POST":
        bookname = request.POST['books']
        authorname = request.POST['authors']
        if bookname == '':
            bookname = "NONE"
        if authorname == '':
            pass
        else:
            firstName, lastName = authorname.split(' ', 1)
        if authorname:
            authorid = Author.objects.get(Q(fisrtname=firstName) & Q(lastname=lastName))
        else:
            authorid = 0
        books = Book.objects.filter(Q(name__icontains=bookname) | Q(author_id=authorid))
        return render(request, 'BrowseBooks.html', {'books': books})
