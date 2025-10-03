from django import forms
from .models import Country
class CountryForm(forms.ModelForm):
 class Meta:
    model = Country
    fields = ['name', 'abrv', 'status']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'abrv': forms.TextInput(attrs={'class': 'form-control'}),
        'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
   }