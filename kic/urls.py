from django.urls import path
from .views import *
from . import views

app_name = 'kic'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('universities/', UniversityView.as_view(), name='university'),
        path(
        'universities/<slug:university_slug>/',
        UniversityDetailView.as_view(),
        name='university_detail',
    ),
    path('training/', TrainingView.as_view(), name='training'),
    path('services/', ServicesView.as_view(), name='services'),
    path('services/<slug:service_slug>/', ServiceDetailView.as_view(), name='service_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact_us, name='contact'),
    path('<slug:country_slug>/', CountryDetailView.as_view(), name='country_detail'),
    path(
        'preparations/<slug:preparation_class_slug>/',
        TestPreparationClassDetailView.as_view(),
        name='preparation_class_detail',
    ),
]
