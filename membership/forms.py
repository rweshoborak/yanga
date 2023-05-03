from django import forms
from django.contrib.auth.models import User
from .models import Registration, Region, District


class RegistrationForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all())
    district = forms.ModelChoiceField(queryset=District.objects.all())

    class Meta:
        model = Registration
        fields = ['reg_number', 'reg_date', 'region', 'district', 'branch']


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name']


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name', 'region']


class UserForm(forms.ModelForm):
    MARITAL_STATUS_CHOICES = (
        ('married', 'Married'),
        ('single', 'Single'),
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    EDUCATION_LEVEL_CHOICES = (
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('tertiary', 'Tertiary'),
        ('higher', 'Higher'),
    )
    phone = forms.CharField(max_length=15)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES)
    occupation = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    education_level = forms.ChoiceField(choices=EDUCATION_LEVEL_CHOICES)
    nida = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'phone', 'date_of_birth',
                  'marital_status', 'occupation', 'gender', 'education_level', 'nida']
        widgets = {
            'password': forms.PasswordInput(),  # Render password field as password input
        }
