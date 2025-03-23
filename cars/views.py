from django.shortcuts import render  # função que já tem no Django
from cars.models import car
from cars.forms import Carform



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
def new_car(request):
    new_car_view = Carform()
    new_car_view.save()
    return render(request, 'new_car.html', {'new_car_view': new_car_view})




