from django.urls import path
from .views import *

app_name = 'kic'

urlpatterns = [
    path('', home, name='home'),
    path('university/', university, name='university'),
    path('training/', training, name='training'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
