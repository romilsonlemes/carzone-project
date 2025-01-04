from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError
from smtplib import SMTPException 
from django.core.exceptions import ImproperlyConfigured
import time
from datetime import datetime

# ----------------------------------------------------------------------

# Create your views here.
def home(request):
    teams = Team.objects.all().order_by('first_name')
    # Other search Features Cars
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    # Other search all Cars
    all_cars = Car.objects.order_by('-created_date')
    # Different options for seachers
    model_search = Car.objects.values_list('model', flat=True).distinct().order_by('model')
    city_search = Car.objects.values_list('city', flat=True).distinct().order_by('city')
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('-year')
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct().order_by('body_style')
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

# ----------------------------------------------------------------------

def about(request):
    teams = Team.objects.all().order_by('first_name')
    data = {
    'teams' : teams,
    }
    return render(request, 'pages/about.html', data)

# ----------------------------------------------------------------------

def services(request):
    return render(request, 'pages/services.html')

# ----------------------------------------------------------------------

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']


        #--------------------------------------------------------------
        # SEND EMAIL
        #--------------------------------------------------------------
        email_subject = f"You have a new message from Carzone website regarding {subject}"
        message_body = f"Name: {name}. Emai: {email}. Phone: {phone}. Message: {message}"

        try:
            #----------------------------------------------------------
                    admin_info = User.objects.get(is_superuser=True)
                    admin_email = admin_info.email

                    start_time = time.time()
                    # Current Time
                    current_time = datetime.now()
                    print(f'Current time: {current_time}')
                    # Format mask the time
                    print("Current Time:", current_time.strftime("%H:%M:%S"))

                    send_mail(
                        email_subject,
                        message_body,
                        'romilsonlemes@gmail.com',
                        [admin_email],
                        fail_silently=False,
                    )
                    end_time = time.time()
                    print(f'Time to send: {end_time - start_time} seconds')
                    messages.success(request, "Thank you for contacting us. We will get back to you shortly.")
                    return redirect('contact')

        except BadHeaderError:
            message_error = "Error: The subject e-mail is invalid."
            print(message_error)
            messages.success(request, message_error)
    
        except SMTPException as e:
            message_error = f"Error to send e-mail: {e}" 
            print(message_error)                
            messages.success(request, message_error)
            #----------------------------------------------------------        

    return render(request, 'pages/contact.html')

# ----------------------------------------------------------------------

def cars(request):
    return render(request, 'cars/cars.html')

# ----------------------------------------------------------------------