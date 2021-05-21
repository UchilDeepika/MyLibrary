from django.urls import path

from .import views

urlpatterns=[
   # path('',views.index,name='index'),   
   # path("studentlogin",views.studentlogin,name="studentlogin"),  
    path('StudentHomePage',views.StudentHomePage,name='StudentHomePage'),   

]