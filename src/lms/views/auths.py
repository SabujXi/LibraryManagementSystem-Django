from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


class SignupView(View):
    template = "lms/auths/signup.html"

    def get(self, request):
        context ={

        }
        return render(request, self.template,context=context)

    def post(self, request):
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']
        username = email
        # TODO: check if user with same email exists
        # create user
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        messages.add_message(request, messages.INFO,
                             f"User successfully registered")
        return redirect('login')


class LoginView(View):
    def get(self, request):
        template = "lms/auths/login.html"
        context = {

        }
        return render(request, template, context=context)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.add_message(request, messages.ERROR,
                                 f"Invalid username/password")
            return redirect('login')
        else:
            login(request, user)
            messages.add_message(request, messages.INFO,
                                 f"Successfully logged in")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def forget_password(request):
    template = "lms/auths/forgetpassword.html"
    context = {

    }
    return render(request, template, context=context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))