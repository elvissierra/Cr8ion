from django.contrib.auth.views import LogoutView 
from django.urls import path
from .views import PrintsDetail

urlpatterns = [
   #path('login/', CustomLoginView.as_view(), name= 'login'),
   path('stls', PrintsDetail.as_view(), name= 'prints'),
   #path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
   #path('register/', RegisterPage.as_view(), name= 'register'),
]