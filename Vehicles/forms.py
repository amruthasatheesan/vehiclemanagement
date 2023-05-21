from django import forms
from django.contrib.auth.models import User
from Vehicles.models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        exclude=("is_active",)
        widgets={
            "purchased_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }