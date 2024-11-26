from django.urls import path
from .views import *


urlpatterns = [
    path('trazado', trazado, name='trazado'),

]
