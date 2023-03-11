
from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def index(request):
    a=[]
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject=request.POST['subject']
        a.append(name)
        a.append(subject)
        if email and message is not ' ':
            send_mail(a,message,'rahulsinghbusiness0101@gmail.com',[email])
            messages.success(request,'Email SENT SUCCESSFULLY CHECK YOUR MAIl')
            return redirect('/')
        else:
            messages.error(request,'Email CANT SEND PLEASE FILL EMAIL IN FIELD AND MESSAGE ')
            return redirect('/')
    else:
        
        return render(request,'id/otp.html')
