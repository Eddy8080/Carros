from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name

class car(models.Model):
    id = models.AutoField(primary_key=True)     # usuário de acesso
    model = models.CharField(max_length=200)    # modelo do carro  
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,related_name='car_brand') # marca
    factory_year = models.IntegerField()        # ano de fabricação
    model_year = models.IntegerField()          # modelo
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null= True)   # valor do carro
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):    #função usada para consultas e melhora a escrita do painel
        return self.model
    

