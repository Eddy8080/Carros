from django.shortcuts import render  # função que já tem no Django
from cars.models import car

# Create your views here.

def cars_view(request):  
    cars = car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = car.filter(model_icontains=search).order_by('model')         
   
    return render(
        request,      #render é para renderizar no HTML
        'cars.html',
        {'cars': cars }                   
    )

