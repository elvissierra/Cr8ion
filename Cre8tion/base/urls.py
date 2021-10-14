from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage, AddDislike, AddLike
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", views.print, name="print"),
    path("print_list/", views.print_list, name="print_list"),
    path("print/<int:pk>/like", views.AddLike, name="like"),
    path("print/<int:pk>/dislike", views.AddDislike, name="dislike"),
    path("print_upload/", views.print_upload, name="print_upload"),
    # path("print_download/", views.print_download, name="print_download")
]
