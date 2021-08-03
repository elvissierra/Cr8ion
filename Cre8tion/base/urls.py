from django import urls
from django.contrib import admin
from django.urls import path, include
from .views import PrintsList


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('base.urls')),
   path('prints_list', PrintsList.as_view(), name= 'prints_list'),
   #path('login/', CustomLoginView.as_view(), name= 'login'),
   #path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
   #path('register/', RegisterPage.as_view(), name= 'register'),
]