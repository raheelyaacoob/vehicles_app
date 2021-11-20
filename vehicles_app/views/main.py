from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path
from django.urls import reverse

from vehicles_app.models import Vehicle


def index_page(request):
    """
    Returns the html template of the home page
    """
    ctx = {
        'vehicles': Vehicle.objects.filter()
    }

    return render(request, 'vehicles.html', ctx)


def vehicle_form(request):
    ctx = {}

    vehicle_id = request.GET.get('id')
    if vehicle_id:
        vehicle_obj = Vehicle.objects.filter(id=vehicle_id).first()
        ctx['vehicle_obj'] = vehicle_obj

    return render(request, "vehicle_form.html", ctx)


def submit_vehicle_form(request):
    """
    Save Vehicle
    """

    data = request.POST
    vehicle_id = data.get('vehicle_id')
    make = data.get('make')
    model = data.get('model')
    speed = data.get('speed')
    average_speed = data.get('average_speed')
    temperature = data.get('temperature')
    fuel_level = data.get('fuel_level')
    engine_status = data.get('engine_status')

    if vehicle_id:
        vehicle_obj = Vehicle.objects.filter(id=vehicle_id).first()
    else:
        vehicle_obj = Vehicle()

    vehicle_obj.make = make
    vehicle_obj.model = model
    vehicle_obj.speed = speed
    vehicle_obj.average_speed = average_speed
    vehicle_obj.temperature = temperature
    vehicle_obj.fuel_level = fuel_level
    vehicle_obj.engine_status = engine_status
    vehicle_obj.save()

    return HttpResponseRedirect(reverse("index_page"))


def delete_vehicle(request):
    vehicle_id = request.GET.get('id')
    print("delete_vehicle for id: ", vehicle_id)

    Vehicle.objects.filter(id=vehicle_id).delete()

    return HttpResponseRedirect(reverse("index_page"))


def view_vehicle(request):
    ctx = {}

    vehicle_id = request.GET.get('id')
    if vehicle_id:
        vehicle_obj = Vehicle.objects.filter(id=vehicle_id).first()
        ctx['vehicle_obj'] = vehicle_obj

    return render(request, "view_vehicle.html", ctx)


urls = [
    path('', index_page, name='index_page'),

    path('vehicle-form', vehicle_form, name='vehicle_form'),
    path('vehicle-save', submit_vehicle_form, name='submit_vehicle_form'),
    path('delete-vehicle', delete_vehicle, name='delete_vehicle'),
    path('view-vehicle', view_vehicle, name='view_vehicle'),
]
