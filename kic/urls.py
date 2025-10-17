from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('university', university, name='university'),
    path('tranning', tranning, name='tranning'),
    path('services', services, name='services'),
    path('aboutUs', aboutUs, name='aboutUs'),
    path('contact', contact, name='contact'),
]
