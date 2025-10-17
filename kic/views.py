from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'kic/index.html')


def university(request):
    return render(request, 'kic/univerisity.html')


def tranning(request):
    return render(request, 'kic/traning.html')

def services(request):
    return render(request, 'kic/services.html')

def aboutUs(request):
    return render(request, 'kic/aboutus.html')

def contact(request):
    return render(request, 'kic/contact.html')
