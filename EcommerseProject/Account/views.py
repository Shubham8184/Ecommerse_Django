# import os
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm,SellerCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# import math
# import random
# import smtplib
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random









def RegisterView(request):
    form=CustomerCreationForm()
    if request.method == 'POST':
        form=CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emailverify')
    template_name='Account/Register.html'
    context={'form':form}
    return render(request,template_name,context)

def LoginView(request):
    try:
        if request.method == 'POST':
            no=request.POST.get('mobile')
            p=request.POST.get('password')
            cuser=CustomUser.objects.filter(mobile_no=no).first()
            if cuser:
                if cuser.is_active:
                    user=authenticate(username=no,password=p)
                    if user and user.is_customer:
                        login(request,user)
                        return redirect('customerhome')
                    else:
                        messages.error(request,'You entered invalid credintial for mobile no.,password or you may not registered as a customer!!')
                        return redirect('login')
                else:
                    messages.error(request,'Still you do not activate your account please activate it below!!')
                    return redirect('emailverify')
            else:
                messages.error(request,'You are not registered yet as a user please register 1st!!!')
        template_name='Account/Login.html'
        context={}
        return render(request,template_name,context)
    except Customer.DoesNotExist:
        return redirect('logout')

def Logoutview(request):
    logout(request)
    return redirect('login')
    
def ShowView(request):
    usr=Customer.objects.all()
    print(usr)
    tempalte_name='Account/Show.html'
    context={'user':usr}
    return render(request,tempalte_name,context)


def SellerRegisterView(request):
    form=SellerCreationForm()
    if request.method == 'POST':
        form=SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selleremailverify')
    template_name='Account/SellerRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def SellerLoginView(request):
    try:
        if request.method == 'POST':
            no=request.POST.get('mobile')
            p=request.POST.get('password')
            suser=CustomUser.objects.filter(mobile_no=no).first()
            if suser:
                if suser.is_active:
                    user=authenticate(username=no,password=p)
                    if user and user.is_seller:
                        login(request,user)
                        return redirect('sellerhome')
                    else:
                        messages.error(request,'You entered invalid credintial for mobile no.,password or you may not registered as a Seller!!')
                        return redirect('sellerlogin')
                else:
                    messages.error(request,'Still you do not activate your account please activate it below!!')
                    return redirect('selleremailverify')
            else:
                messages.error(request,'You are not registered yet as a user please register 1st!!')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')
        # user=authenticate(username=no,password=p)
        # if user and user.is_seller:
        #     login(request,user)
        #     return redirect('sellerhome')
        # messages.error(request,'You are not a Seller')
    template_name='Account/SellerLogin.html'
    context={}
    return render(request,template_name,context)

def SellerLogoutview(request):
    logout(request)
    return redirect('sellerlogin')

def SellerShowView(request):
    usr=Seller.objects.all()
    print(usr)
    tempalte_name='Account/SellerShow.html'
    context={'user':usr}
    return render(request,tempalte_name,context)


# def Customerverificatonview(request):
#     digits="0123456789"
#     OTP=""
#     for i in range(6):
#         OTP+=digits[math.floor(random.random()*10)]
#     otp = OTP + " is your OTP"
#     msg= otp
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.starttls()
#     s.login("Your Gmail Account", "You app password")
#     emailid = input("Enter your email: ")
#     s.sendmail('&&&&&&&&&&&',emailid,msg)
#     a = input("Enter Your OTP >>: ")
#     if a == OTP:
#         print("Verified")
#     else:
#         print("Please Check your OTP again")

#Email OTP Verification View Code--------

def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        print(random.random()*10)
        print(math.floor(random.random() * 10))
        # print(digits[math.floor(random.random() * 10)])
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
#0.1*10=1.0 -->>1
#0.4*10=4.0 -->>4
 


def send_otp(request):
    email=request.POST.get("email")
    user=CustomUser.objects.all()
    # for i in user:
        # if email == i.email :
    print(email)
    o=generateOTP()
    print(o)
    htmlgen = 'Your OTP is '+o
    send_mail('OTP request',htmlgen,'bobadesp1234@gmail.com',[email],fail_silently=True)
    return HttpResponse(o)
    # else:
    #     print('Email is not Not Found')
    #     messages.error(request,'Entered email does not exist please enter Registered email address...!!!')
    #     return redirect('emailverify')
    


def CustomerEmailVerificationview(request):
    template_name='Account/Customeremailverify.html'
    context={}
    return render(request,template_name,context)

def Customeractivateview(request):
    try:
        email=request.POST.get('email')
        customer=CustomUser.objects.get(email=email)
        customer.is_active=True
        customer.save()
        return render('login')
    except Customer.DoesNotExist:
        return redirect('logout')



def SellerEmailVerificationview(request):
    template_name='Account/Selleremailverify.html'
    context={}
    return render(request,template_name,context)

def Selleractivateview(request):
    try:
        email=request.POST.get('email')
        customer=CustomUser.objects.get(email=email)
        customer.is_active=True
        customer.save()
        return redirect('sellerlogin')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')



def Customerpassview(request):
    form=SetPasswordForm(request.user)
    template_name='Account/Customerforgotpass.html'
    context={'form':form}
    return render(request,template_name,context)

def Customerpasswordforgotview(request):
    try:
        print(request.POST)
        email=request.POST.get('email')
        print(email)
        customer=CustomUser.objects.get(email=email)
        print(customer)
        password=request.POST.get('new_password2')
        print(password)
        cnpass=str(password)
        customer.set_password(cnpass)
        customer.save()
        return redirect('customerhome')
    except Customer.DoesNotExist:
        return redirect('logout')


def Sellerpassview(request):
    form=SetPasswordForm(request.user)
    template_name='Account/Sellerforgotpass.html'
    context={'form':form}
    return render(request,template_name,context)

def Sellerpasswordforgotview(request):
    try:
        print(request.POST)
        email=request.POST.get('email')
        print(email)
        seller=CustomUser.objects.get(email=email)
        print(seller)
        password=request.POST.get('new_password2')
        print(password)
        cnpass=str(password)
        seller.set_password(cnpass)
        seller.save()
        return redirect('sellerhome')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')


def Customerchangepassview(request):
    form=PasswordChangeForm(request.user)
    if request.method == 'POST':
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('customerhome')
        else:
            messages.error(request,'Please check your password once!!')
    template_name='Account/Customerchangepass.html'
    context={'form':form}
    return render(request,template_name,context)

def Sellerchangepassview(request):
    form=PasswordChangeForm(request.user)
    if request.method == 'POST':
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('sellerhome')
        else:
            messages.error(request,'Please check your password once!!')
    template_name='Account/Sellerchangepass.html'
    context={'form':form}
    return render(request,template_name,context)
