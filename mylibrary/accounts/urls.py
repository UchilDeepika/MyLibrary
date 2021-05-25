from django.urls import path

from .import views

urlpatterns=[
    path('',views.index,name='index'),   
    path("studentregister",views.studentregister,name="studentregister"),  
    path("studentlogin",views.studentlogin,name="studentlogin"),  
    path("studentlogout",views.studentlogout,name="studentlogout"),  

]