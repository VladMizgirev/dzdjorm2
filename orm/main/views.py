from django.http import Http404
from django.shortcuts import render

from main.models import Car


def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    return render(request, template_name, {"cars_list": cars})


def car_details_view(request, car_id):
    try:
        filtered_objects = Car.objects.filter(id=car_id)
        template_name = 'main/details.html'
        return render(request, template_name, {'filtered_objects': filtered_objects})
    except Car.DoesNotExist:
        raise Http404('Car not found')



def sales_by_car(request, car_id):
    try:
        filtered_car = Car.objects.filter(id=car_id)
        template_name = 'main/sales.html'
        return render(request, template_name, {"filtered_car": filtered_car})  
    except Car.DoesNotExist:
        raise Http404('Car not found')
