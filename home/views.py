from django.shortcuts import render
from datetime import datetime
def homepage_view(request):
    context={
        'restaurant_name': 'Spice Symphony'
    }
    return render(request, 'homepage.html', context)

def contact_view(request):
    return render(request, 'home/contact.html')

def reservations(request):
    context={
        'current-year': datetime.now().year
    }
    return render(request, 'reservations.html', context)