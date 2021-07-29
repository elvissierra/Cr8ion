#from django.contrib.auth.views import LogoutView 
from django.urls import path
from .views import PrintsList


urlpatterns = [
   #path('login/', CustomLoginView.as_view(), name= 'login'),
   path('prints_list', PrintsList.as_view(), name= 'prints_list'),
   #path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
   #path('register/', RegisterPage.as_view(), name= 'register'),
]