from django.contrib.auth.models import AbstractUser, User, Group, Permission
from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Registration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=20)
    reg_date = models.DateField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='my_users')
    # Specify a custom related name for the 'user_permissions' field
    user_permissions = models.ManyToManyField(Permission, related_name='my_users_permissions')
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    MARITAL_STATUS_CHOICES = (
        ('married', 'Married'),
        ('single', 'Single'),
    )
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    occupation = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    EDUCATION_LEVEL_CHOICES = (
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('tertiary', 'Tertiary'),
        ('higher', 'Higher'),
    )
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    nida = models.CharField(max_length=20)

    def __str__(self):
        return self.marital_status
