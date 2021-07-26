from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm

#* CUSTOM LOGIN VIEW
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('home')) 
            else:
                messages.error(request,'Please click the link in the activation mail sent to your registered mail id to activate your account')
                return redirect(reverse('home'))
        else:
            messages.error(request,'username or password not correct')
            return redirect(reverse('home'))
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})
