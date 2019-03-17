from django.shortcuts import render
from .forms import UserForm,UserPortfolioForm
from basicapp import models
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in ! Nice")
@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basicapp:index'))
def register(request):
    registered=False

    if request.method == "POST":
        userform=UserForm(data=request.POST)
        profileform=UserPortfolioForm(data=request.POST)

        if userform.is_valid() and profileform.is_valid():

            user=userform.save()
            user.set_password(user.password) # for hashing the password_validation
            user.save()

            profile=profileform.save(commit=False)
            profile.user=user

            if 'picture' in request.FILES: # for any pdf csv or image use request.FILES
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        else:
            print(userform.errors,profileform.errors)
    else:
        userform=UserForm()
        profileform=UserPortfolioForm()

    return render(request,'basicapp/registration.html',
                                                   {'userform':userform,
                                                   'profileform':profileform,
                                                   'registered':registered})
def userlogin(request):

    if request.method  == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basicapp:index'))
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('Invalid credentials')
    else:
        return render(request,'basicapp/login.html')
