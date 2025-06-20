from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from user.models import Profile

# Create your views here.

def login_signup_view(request):
    if request.method == 'POST':
        # Handle Login
        if 'signin' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to home page after login
            else:
                messages.error(request, 'Invalid username or password')

        # Handle Signup
        elif 'signup' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
            else:
                try:
                    user = User.objects.create_user(
                        username=username, 
                        email=email, 
                        password=password
                    )
                    login(request, user)
                    return redirect('/')
                except Exception as e:
                    messages.error(request, f'Error creating user: {e}')

    return render(request, 'user/login_signup.html')

def logout_view(request):
    logout(request)
    return redirect('user:login_signup')

class Profile_View(ListView):
    model = Profile
    template_name = "user/profile.html"
    context_object_name = 'person'