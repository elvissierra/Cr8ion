from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.CustomLoginView, name= 'login'),

]