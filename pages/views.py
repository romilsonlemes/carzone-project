from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all().order_by('first_name')
    # Other search Features Cars
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    # Other search all Cars
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all().order_by('first_name')
    data = {
    'teams' : teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def cars(request):
    return render(request, 'pages/cars.html')

def contact(request):
    return render(request, 'pages/contact.html')

def carDetails(request):
    return render(request, 'pages/car-details.html')