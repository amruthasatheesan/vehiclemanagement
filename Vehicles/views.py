from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from Vehicles.forms import VehicleForm
from Vehicles.models import Vehicle
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,UpdateView,DeleteView,DetailView,ListView
# Create your views here.




class VehicleCreateView(CreateView):
    model=Vehicle
    template_name="vehicle-add.html"    
    form_class=VehicleForm
    success_url=reverse_lazy("vehicle-list")


class VehicleListView(ListView):
    model=Vehicle
    template_name="vehicle-list.html"
    context_object_name="vehicle"


class VehicleDetailView(DetailView):
    model=Vehicle
    template_name="vehicle-detail.html"
    context_object_name="vehicle"


class VehicleEditView(UpdateView):
    model=Vehicle
    form_class=VehicleForm
    template_name="vehicle-edit.html"
    success_url=reverse_lazy("vehicle-list")


def vehicle_delete_view(request,*args,**kwargs):
    id=kwargs.get('pk')
    Vehicle.objects.get(id=id).delete()
    return redirect('vehicle-list')



class IndexView(TemplateView):
    template_name="index.html"    





