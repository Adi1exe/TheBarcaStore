from django import forms
from .models import Accessory

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'price', 'image']