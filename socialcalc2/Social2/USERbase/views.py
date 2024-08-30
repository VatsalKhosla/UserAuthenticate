from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer

@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'name':"vatsal",age:23}))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "USERbase/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "USERbase/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "USERbase/register.html")

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        emailaddress=request.POST['emailadress']
        password = request.POST['password']

        user = authenticate(request, username=username,emailaddress=emailaddress, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')      
        else:
            messages.success(request,("There was an error Logging in, Try Again..."))
            return redirect('login')

    else:
     return render(request, 'authenticate/login.html',{})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index")) 
