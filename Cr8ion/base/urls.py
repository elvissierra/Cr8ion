from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.print, name="print"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("print_list/", views.print_list, name="print_list"),
    path("likes/", views.likes, name="likes"),
    path("print_upload/", views.print_upload, name="print_upload"),
    # path()
]
