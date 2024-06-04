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
