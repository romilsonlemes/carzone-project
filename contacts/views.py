from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError
from smtplib import SMTPException 
from django.core.exceptions import ImproperlyConfigured
import time
from datetime import datetime

# Create your views here.
def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made in inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+ car_id)



        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name, last_name=last_name, customer_need=customer_need,
                          city=city, state=state, email=email, phone=phone, message=message)
        

        try:
                confirm_send_Email = False
                #Send email
                #--------------------------------------------------------------------------------------------
                admin_info = User.objects.get(is_superuser=True)
                admin_email = admin_info.email

                start_time = time.time()
                # Current Time
                current_time = datetime.now()
                print(f'Current time: {current_time}')
                # Format mask the time
                print("Current Time:", current_time.strftime("%H:%M:%S"))

                send_mail(
                    'New Car Inquiry',
                    'You have a new inquiry for the car ' + car_title + '. Please login to your afmin panel for more info.',
                    'romilsonlemes@gmail.com',
                    [admin_email, 'romilson.lemescordeiro@edu.sait.ca'],
                    fail_silently=False,
                )
                confirm_send_Email = True
                end_time = time.time()
                print(f'Time to send: {end_time - start_time} seconds')

        except BadHeaderError:
            confirm_send_Email = False
            print("Error: The subject e-mail is invalid.")
    
        except SMTPException as e:
            confirm_send_Email = False
            print(f"Error to send e-mail: {e}")                
    

        if confirm_send_Email == True:
            # Save Contacts
            #--------------------------------------------------------------------------------------------
            contact.save()
            messages.success(request, 'Your request has been submitted, we will get bacj o your shortly.')
            return redirect('/cars/'+ car_id)
            #--------------------------------------------------------------------------------------------
        
