from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('cars', views.cars, name='cars'),
    # path('carDetails', views.carDetails, name='carDetails'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
]
