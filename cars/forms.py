from django import forms
from cars.models import Brand




class Carform(forms.Form):    
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    valeu = forms.FloatField()
    photo = forms.ImageField()

def __str__(self):
    return self.model

    
    
    