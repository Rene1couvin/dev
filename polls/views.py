from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#  login  # Import login as auth_login
from .forms import AuthenticationForm, SignupForm 

def home(request):
    return render(request,'before/home.html')

def about(request):
    return render(request,'before/about.html')

def service(request):
    return render(request,'before/services.html')

def contact(request):
    return render(request,'before/contactus.html')

def reserve(request):
    return render(request,'after/reservep.html')

@login_required
def ahome(request):
    return render(request,'after/Home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('ahome')  # Redirect to a success page after login
            else:
                # If the user couldn't be authenticated, return an error message
                form.add_error(None, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('ahome')  # Redirect to a success page after signup
            else:
                return redirect('login')  # Redirect to login page if authentication fails
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})





# def signup(request):
#     if request.method == 'POST':

#         form = SignupForm(request.POST)
        
#         if form.is_valid():
#             # Check if passwords match
#             username = form.cleaned_data['username']
#             raw_password = form.cleaned_data['password']
#             user = form.save()
#             # Log the user in
#             username = form.cleaned_data['username']
#             raw_password = form.cleaned_data['password']
#             user = authenticate(username=username, password=raw_password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('login')  # Redirect to a success page after signup
#             else:
#                 return redirect('auth/login.html')  # Redirect to login page if authentication fails
#     else:
#         form = SignupForm()
#     return render(request, 'auth/signup.html', {'form': form})




def profile_view(request):
    return render(request, 'after/profile/profile.html', {'user': request.user})