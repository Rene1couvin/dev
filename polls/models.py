from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    idNumber = models.IntegerField(unique=True ,default='')
    phone = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=255, default='')
    password = models.CharField(null=False,max_length=100, default='')

    groups = models.ManyToManyField('auth.Group', related_name='polls_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='polls_users')

    def save(self, *args, **kwargs):
        if self.pk is None:  # Check if the user is being created (not updated)
            self.password = make_password(self.password)  # Hash the password
        super(User, self).save(*args, **kwargs)


class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class ParkingPlace(models.Model):
    name = models.CharField(max_length=100, verbose_name='Parking Place Name')
    address = models.CharField(max_length=255, verbose_name='Address')
    phone = models.IntegerField( verbose_name='Phone')
    
    
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor')
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, verbose_name='Condition of the Parking Place')
    
    photo1 = models.ImageField(upload_to='parking_place_photos', verbose_name='Photo 1')
    photo2 = models.ImageField(upload_to='parking_place_photos', verbose_name='Photo 2')
    photo3 = models.ImageField(upload_to='parking_place_photos', verbose_name='Photo 3')
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_place = models.ForeignKey(ParkingPlace, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    