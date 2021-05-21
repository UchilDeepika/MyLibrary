from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
# Create your views here.
def index(request):
    return render(request,'index.html')

def studentlogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('StudentHomePage')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('StudentLogin.html')
    else:
        return render(request,'StudentLogin.html')

def studentregister(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info("Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.info("Email already exists")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()                
                return redirect('studentlogin')
        else:
            messages.info("Passwords not matching")
            return redirect('studentregister')
        return redirect( '/')
    else:
        return render(request,'StudentRegister.html')