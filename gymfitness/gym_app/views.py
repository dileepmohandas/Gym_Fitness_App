from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method =='POST':
        username = request.POST['usernumber']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2= request.POST['pass2']
        

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Usernumber already exists')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('/signup')
            else:

                myuser=User.objects.create_user(username,email,pass1)
                myuser.save()
                messages.success(request,"User is Created Please Login")
                return redirect('/login')
        
        else:
            messages.error(request,'Password Not Equal')
            return redirect('/signup')

    return render(request,'signup.html')

def login_user(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"login.html")

def logout_user(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')