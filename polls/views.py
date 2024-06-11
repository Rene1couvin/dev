
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import *
from .models import ParkingPlace
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ParkingPlaceForm
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'before/home.html')

@login_required
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
                return redirect('ahome') 
            else:
                
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
                return redirect('ahome')  
            else:
                return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})



@login_required
def profile_view(request):
    return render(request, 'after/profile/profile.html', {'user': request.user})

@login_required
def parkingplace(request):
    parkingplace = ParkingPlace.objects.all()
    return render(request, 'after/parkingplace.html', {'parkingplace': parkingplace})

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
       
        subject = f"New message from {name}"
        message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_list = ['renefrancisco808@gmail.com']
        
  
        send_mail(subject, message_body, email, recipient_list)
        
        return HttpResponse("Thank you for your message.")
    else:
        return redirect('before/home')

@login_required
def add(request):
    if request.method == 'POST':
        form = ParkingPlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('parkingplace')  
    else:
        form = ParkingPlaceForm()
    return render(request, 'after/add.html', {'form': form})




from django.shortcuts import render, redirect, get_object_or_404
from .models import ParkingPlace
from .forms import ReservationForm
@login_required
def parking_places_list(request):
    parking_places = ParkingPlace.objects.all()
    return render(request, 'after/parkingplaces.html', {'parking_places': parking_places})

@login_required
def reserves(request, pk):
    parking_place = get_object_or_404(ParkingPlace, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.parking_place = parking_place
            reservation.user = request.user
            reservation.save()
            return redirect('ahome') 
    else:
        form = ReservationForm(initial={'parking_place': parking_place, 'user': request.user})

    return render(request, 'parking/reserve_spot.html', {'form': form, 'parking_place': parking_place})

def placep(request):
    return render(request,'after/parkingplaces.html')