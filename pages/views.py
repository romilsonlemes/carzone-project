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
    # Different options for seachers
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams' : teams,
        'featured_cars' : featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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

def contact(request):
    return render(request, 'pages/contact.html')

def cars(request):
    return render(request, 'cars/cars.html')

# def carDetails(request):
#     return render(request, 'pages/car_details.html')