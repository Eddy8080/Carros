from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import new_car_view



urlpatterns = [
    path('admin/',admin.site.urls),
    path('car/', new_car_view, name='new_car'),
    path('new_car/', new_car_view, name='new_car'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











