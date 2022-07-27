from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from asosiy.models import *
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")

    def post(self, request):
        u = request.POST.get("l")
        p = request.POST.get("p")
        users = authenticate(username=u,password=p)
        if users is None:
            return redirect("/login/")
        login(request, users)
        return redirect("/home/")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("login")

class RegisterView(View):
    def get(self, request):
        return render(request, "page-user-register.html")

    def post(self,request):
        if request.POST.get("p") == request.POST.get("rp"):
            u = User.objects.create_user(
                username=request.POST.get("i"),
                password=request.POST.get("p"),
            )
            Accaunt.objects.create(
                ism = request.POST.get("i"),
                email = request.POST.get("e"),
                jins = request.POST.get("gender"),
                shahar = request.POST.get("sh"),
                mamlakat = request.POST.get("m"),
                user = u
            )
            return redirect("/home/")
        else:
            return redirect("/register/")
