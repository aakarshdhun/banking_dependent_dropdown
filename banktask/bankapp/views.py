from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bankapp.forms import ProcessDataForm
from bankapp.models import District, Branch, ProcessData


# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Enter valid Username or Password')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
def username(request):
    use=User.objects.all()
    return render(request,'username.html',{'user':use})

def register(request):
    if request.method =='POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        if password == confirm_password :
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is taken. Try another name.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Password did not matched.")
            return redirect('register')
    return render(request,'register.html')
def form(request):
    template_name = 'form.html'
    district = District.objects.all()
    branch = Branch.objects.all()

    return render(request, template_name, {'district': district, 'branch': branch})

def process(request):
    # if request.method=='POST':
        # name = request.POST.get('name')
        # dob = request.POST.get('dob')
        # age = request.POST.get('age')
        # gender = request.POST.get('gender')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # address = request.POST.get('address')
    pdata=ProcessDataForm(request.POST or None)
    if pdata.is_valid():
        pdata.save()
        return redirect('thankyou')
    # else:
    #     messages.info(request,'Please fill the details')
    #     return render(request,'form.html')
    return render(request,'form.html')
def thankyou(request):
    return render(request,'thankyou.html')
def thrissur(request):
    return render(request,'thrissur.html')
def palakkad(request):
    return render(request,'palakkad.html')
def ernakulam(request):
    return render(request,'ernakulam.html')
def calicut(request):
    return render(request,'calicut.html')
def trivandrum(request):
    return render(request,'trivandrum.html')