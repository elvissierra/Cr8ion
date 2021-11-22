from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView
from .models import Print
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from .forms import PrintForm

# User Registration
class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("print")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_autenticated:
            return redirect("print")
        return super(RegisterPage, self).get(*args, **kwargs)


# Login
class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("print")


# Home Page/ Print rendering
def print(request):
    prints = Print.objects.all()
    return render(request, "base/print.html", {"prints": prints})


class PrintView(ListView):
    model = Print
    context_object_name = "print"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["print"] = context["print"].filter(user=self.request.user)
        context["count"] = context["print"].count()

        search_input = self.request.GET.get("search-area", "")
        if search_input:
            context

        return context


# Print List
def print_list(request):
    prints = Print.objects.all()
    paginator = Paginator(prints, 12)
    page_number = request.GET.get("page")
    prints = paginator.get_page(page_number)
    return render(request, "base/print_list.html", {"prints": prints})


# Uploading Files
def print(request):
    prints = Print.objects.all()
    return render(request, "base/print.html", {"prints": prints})


def print_upload(request):
    if request.method == "POST":
        form = PrintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("print_list")
        else:
            form = PrintForm()
    else:
        form = PrintForm()

    return render(request, "base/print_upload.html", {"form": form})
