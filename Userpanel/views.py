from django.shortcuts import render,redirect

# Create your views here.

def sidebar(request):
    return render(request,"user/sidebar.html")

def home(request):
    return render(request,"user/index.html")

def car(request):
    return render(request,"user/car.html")

def cardetails(request):
    return render(request,"user/cardetails.html")


def payment(request):
    return render(request,"user/payment.html")

def login(request):
    return render(request,"user/login.html")

def forgot_password(request):
    return render(request,"user/forgot_password.html")

def signup(request):
    return render(request,"user/signup.html")


def twowheeler(request):
    return render(request,"user/2wheeler.html")

def about(request):
    return render(request,"user/about.html")


def feedback(request):
    return render(request,"user/feedback.html")
