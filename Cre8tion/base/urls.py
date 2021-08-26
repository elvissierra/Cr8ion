from django.urls import path
from . import views

# from . views import PrintsList

urlpatterns = [
    path("", views.index, name="index"),
    path("index1", views.index1, name="index1")
    # path('',PrintsList.as_view(), name= 'prints_list'),
    # path('login/', CustomLoginView.as_view(), name= 'login'),
    # path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    # path('register/', RegisterPage.as_view(), name= 'register'),
]
