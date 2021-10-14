from typing import Counter
from django.contrib.auth import views
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse
from django.views.generic.base import View
from .forms import PrintForm
from .models import Print
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy, reverse
from .forms import PrintForm

# USER REGISTRATION
class RegisterPage(FormView):
    template_name = "main/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("print")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("print")
        return super(RegisterPage, self).get(*args, **kwargs)


# USER LOGIN
class CustomLoginView(LoginView):
    template_name = "main/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("print")


# HOME PAGE
class PrintView(ListView):
    model = Print
    context_object_name = "print"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["print"] = context["print"].filter(user=self.request.user)
        context["count"] = context["print"].count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["print"] = context["print"].filter(title__contains=search_input)

        context["search_input"] = search_input

        return context


# PRINT LIST
def print_list(request):
    prints = Print.objects.all()
    paginator = Paginator(prints, 12)
    page_number = request.GET.get("page")
    prints = paginator.get_page(page_number)
    return render(request, "main/print_list.html", {"prints": prints})


# ORDER PRINTS BY DOWNLOAD COUNTS


# LIKES AND DISLIKES
def LikeView(request, pk):
    print = get_object_or_404(Print, id=request.POST.get("print_id"))
    print.likes.add(request.user)
    return HttpResponseRedirect(reverse("article_detail", args=[str(pk)]))


# UPLOAD FILES
def print(request):
    prints = Print.objects.all()
    return render(request, "main/print.html", {"prints": prints})


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
    return render(request, "main/print_upload.html", {"form": form})
