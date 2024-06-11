# polls/forms.py

from django import forms
from .models import User, Reservation, ParkingPlace


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'idNumber', 'username', 'phone', 'email', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=254,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
class ParkingPlaceForm(forms.ModelForm):
    class Meta:
        model = ParkingPlace
        fields = ['name', 'address', 'phone', 'condition', 'photo1', 'photo2', 'photo3']
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = []