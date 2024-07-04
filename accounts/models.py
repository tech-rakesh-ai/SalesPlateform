from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Address(models.Model):
    address = models.TextField()
    # Add other address fields as needed


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    # Add other custom user fields as needed

    objects = UserManager()

    def __str__(self):
        return self.username
