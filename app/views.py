
from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
# from app.models import Student
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
import json
from django.core.mail import send_mail
import math, random


# Create your views here.



def login(request):
    return render(request, 'id/login.html')


def welcome(request):
    return render(request, 'id/welcome.html')

def otp(request):
    return render(request, 'id/otp.html')





def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.GET.get   ("email")
     print(email)
     o=generateOTP()
     htmlgen = '<p>Your OTP is <strong>o</strong></p>'
     send_mail('OTP request',o,'<your gmail id>',[email], fail_silently=False, html_message=htmlgen)
     return HttpResponse(o)



    

    
        






# Create your views here.
