from django import forms
from cars.models import Brand


class Carform(forms.ModelForm):
    class Meta:
        model = forms.CharField(max_length=200)
        brand = forms.CharField(max_length=200)
        factory_year = forms.IntegerField()
        model_year = forms.IntegerField()
        plate =forms.CharField(max_length=10)
        value = forms.ImageField()
        photo = forms.ImageField()
        
