from django.urls import path

from .import views

urlpatterns = [
    # path('',views.index,name='index'),
    # path("studentlogin",views.studentlogin,name="studentlogin"),
    path('StudentHomePage', views.StudentHomePage, name='StudentHomePage'),
    path('BookDetails', views.BookDetails, name='BookDetails'),
    path('CheckOut', views.CheckOut, name='CheckOut'),
    path('', views.index, name='index'),
    path('returnbook', views.returnbook, name='returnbook'),
    path('BooksSearch', views.BooksSearch, name='BooksSearch'),
    path('AuthorSearch', views.AuthorSearch, name='AuthorSearch'),
    path('BrowseBooks', views.BrowseBooks, name='BrowseBooks'),
    path('SearchedBooks', views.SearchedBooks, name='SearchedBooks')
]
