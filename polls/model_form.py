from django.forms import ModelForm
from django import forms

from .models import Creative, Location


class CreativeForm(ModelForm):
    class Meta:
        model = Creative
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"})
        }

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            "panel_id": forms.TextInput(attrs={"class": "form-control"})
        }