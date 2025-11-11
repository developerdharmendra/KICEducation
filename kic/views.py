from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'kic/index.html')


def university(request):
    return render(request, 'kic/univerisity.html')


def training(request):
    return render(request, 'kic/training.html')

def services(request):
    return render(request, 'kic/services.html')

def about(request):
    return render(request, 'kic/about.html')

def contact(request):
    return render(request, 'kic/contact.html')
