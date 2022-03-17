from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def vehicle(request):
    return render(request,"all-driver.html")

def books(request):
    return render(request,"book.html")

def register(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            first_name = request.POST['first_name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            password = request.POST['pass']
            Address = request.POST['Address']
            cpass = request.POST['cpass']
            user_type = request.POST['type']
            gender = request.POST['gender']
            user = User.objects.filter(email=email)
            if user:
                messages.error(request, "User already exists!!!")
                return redirect("register")
            else:
                if cpass==password:
                    user = User.objects.create_user(email=email, password=password,first_name=first_name,mobile_no=mobile,address=Address,gender=gender)
                    if user_type=='customer':
                        user.is_customer=True
                        user.save()
                        return redirect("Login")
                    else:
                        user.is_driver=True
                        user.save()
                        return redirect("Login")
                else:
                    messages.error(request, "Password didn't match!!!")
                    return redirect("register")
        return render(request,"form.html")
    else:
        return redirect("index")

def Login(request):
    if not request.user.is_authenticated:
        if request.method  == 'POST':
            email = request.POST['uname']
            password = request.POST['psw']
            user = authenticate(email = email,password = password)
            if user:
                login(request, user)
                messages.success(request, "Login Successfully!!!")
                if request.user.is_driver:
                    return redirect("index")
                elif request.user.is_superuser:
                    return redirect("index")
                else:
                    return redirect("index")
            else:
                messages.error(request, "Please check email and password!!!")
                return redirect("Login")
        return render(request,"login.html")
    else:
        return redirect("index")


def user_logout(request):
    logout(request)
    return redirect("index")


def dashboard(request):
    return render(request, "Head/dashboard.html")


def customer(request):
    user = User.objects.filter(is_customer=True)
    return render(request, "Head/view_custome.html",{'user':user})

def driver(request):
    user = User.objects.filter(is_driver=True)
    return render(request, "Head/view_driver.html",{'user':user})

def booking(request):
    book = Booking.objects.all()
    return render(request, "Head/booking.html",{'book':book})



#Driver Work


def add_vehical_detail(request):
    data = Vehical.objects.filter(user=request.user)
    if data:
        return render(request, "driver/edit-vehical-detail.html",{'data':data})
    else:
        if request.method=='POST':
            user = request.user
            number = request.POST['number']
            name = request.POST['name']
            image = request.FILES['image']
            price = request.POST['price']
            vehicle_type = request.POST['vehicle_type']
            driver_type = request.POST['driver_type']
            contact = request.POST['contact']
            Vehical.objects.create(user=user,vehical_no=number,vehical_image=image,owner_name=name,contact=contact,price=price,vehical_type=vehicle_type,travel_type=driver_type)
            return redirect("add_vehical_detail")
        return render(request, "driver/add_vehical_detail.html")

def change_password(request):
    if request.method=='POST':
        current_pass = request.POST['op']
        new_pass = request.POST['p']
        c_pass = request.POST['cp']
        if c_pass!=new_pass:
            messages.error(request, "Please Check Password")
            return redirect("change_password")
        else:
            user = User.objects.get(email=request.user)
            p = user.check_password(current_pass)
            if p==True:
                user.set_password(new_pass)
                user = authenticate(email=user,password=new_pass)
                if user:
                    login(request,user)
                    messages.success(request,"Password Change !!!") 
                    return redirect("driver_dashboard")
    return render(request, "driver/change-password.html")

def edit_vehical_detail(request):
    data = Vehical.objects.get(user=request.user)
    if request.method=='POST':
        user = request.user
        price = request.POST['price']
        contact = request.POST['contact']
        Vehical.objects.filter(user=user).update(price=price,contact=contact)
        return redirect("edit_vehical_detail")
    return render(request, "driver/edit-vehical-detail.html",{'data':data})

def book(request):
    b = Booking.objects.filter(user=request.user)
    return render(request, "Head/view_custome.html")

def driver_dashboard(request):
    return render(request,"driver/dashboard.html")