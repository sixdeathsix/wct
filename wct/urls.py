from django.contrib import admin
from django.urls import path, include
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('importance', importance, name='importance'),
    path('predicted', predicted, name='predicted'),
    path('difference', difference, name='difference'),
    path('forecastwell', forecastwell, name='forecastwell'),
    path('forecastwell', forecastwell, name='forecastwell'),
    path('onewell/<int:id>', onewell, name='onewell'),
    path('auth/', include('django.contrib.auth.urls')),
]