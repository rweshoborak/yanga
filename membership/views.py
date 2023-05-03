from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration, Region, District, User
from .forms import RegistrationForm, RegionForm, DistrictForm


def home(request):
    # Add your logic for the home view here
    # For example, you can retrieve data from models and pass it to the template
    members = User.objects.all()
    reg = Registration.objects.all()
    context = {
        'message': 'Karibu Tawi la YANGA ROCK CITY MWANZA',
        'member': members,
        'Registered': reg,
    }
    return render(request, 'membership/index.html', context)


# View for creating a new registration
def registration_create(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registration_list')
    context = {
        'form': form,
    }
    return render(request, 'registration_create.html', context)


# View for updating an existing registration
def registration_update(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    form = RegistrationForm(request.POST or None, instance=registration)
    if form.is_valid():
        form.save()
        return redirect('registration_list')
    context = {
        'form': form,
    }
    return render(request, 'registration_update.html', context)


# View for deleting a registration
def registration_delete(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('registration_list')
    context = {
        'registration': registration,
    }
    return render(request, 'registration_delete.html', context)


# View for listing all registrations
def registration_list(request):
    registrations = Registration.objects.all()
    context = {
        'registrations': registrations,
    }
    return render(request, 'registration_list.html', context)


# View for displaying details of a single registration
def registration_detail(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    context = {
        'registration': registration,
    }
    return render(request, 'registration_detail.html', context)


# View for creating a new region
def region_create(request):
    form = RegionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('region_list')
    context = {
        'form': form,
    }
    return render(request, 'region_create.html', context)


# View for updating an existing region
def region_update(request, pk):
    region = get_object_or_404(Region, pk=pk)
    form = RegionForm(request.POST or None, instance=region)
    if form.is_valid():
        form.save()
        return redirect('region_list')
    context = {
        'form': form,
    }
    return render(request, 'region_update.html', context)


# View for deleting a region
def region_delete(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        region.delete()
        return redirect('region_list')
    context = {
        'region': region,
    }
    return render(request, 'region_delete.html', context)


# View for listing all regions
def region_list(request):
    regions = Region.objects.all()
    context = {
        'regions': regions,
    }
    return render(request, 'region_list.html', context)


# View for displaying details of a single region
def region_detail(request, pk):
    region = get_object_or_404(Region, pk=pk)
    context = {
        'region': region,
    }
    return render(request, 'region_detail.html', context)


# View for creating a new district
def district_create(request):
    form = DistrictForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('district_list')
    context = {
        'form': form,
    }
    return render(request, 'district_create.html', context)


# View for updating an existing district
def district_update(request, pk):
    district = get_object_or_404(District, pk=pk)
    form = DistrictForm(request.POST or None, instance=district)
    if form.is_valid():
        form.save()
        return redirect('district_list')
    context = {
        'form': form,
    }
    return render(request, 'district_update.html', context)


# View for deleting a district
def district_delete(request, pk):
    district = get_object_or_404(District, pk=pk)
    if request.method == 'POST':
        district.delete()
        return redirect('district_list')
    context = {
        'district': district,
    }
    return render(request, 'district_delete.html', context)


# View for listing all districts
def district_list(request):
    districts = District.objects.all()
    context = {
        'districts': districts,
    }
    return render(request, 'district_list.html', context)


# View for displaying details of a single district
def district_detail(request, pk):
    district = get_object_or_404(District, pk=pk)
    context = {
        'district': district,
    }
    return render(request, 'district_detail.html', context)
