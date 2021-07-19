from django.urls import path
from . import views

urlpatterns = [
    path('',views.threedModels, name='3dmodels'),
]