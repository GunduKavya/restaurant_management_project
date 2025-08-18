from django.shortcuts import render
def homepage_view(request):
    context={
        'restaurant_name': 'Spice Symphony'
    }
    return render(request, 'homepage.html', context)