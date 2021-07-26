from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.http import request
from django.shortcuts import render, redirect
from .models import Prints


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

class RegisterPage(FormView):
    template_name= 'base/register.html'
    form_class = UserCreationForm
    redirect_authentication_user = True
    success_url = reverse_lazy ('prints')

    def form_valid(self, form):
        user = form.save()
        if user != None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, args, kwargs):
        if self.request.user.is_authenticated:
            return redirect('prints')
        return super(RegisterPage, self).get(args, kwargs)

class PrintsDetail(LoginRequiredMixin, DetailView):
    model = Prints
    context_object_name = 'print'
    template_name = 'base/detail.html'

#class PrintsUpload
#
#class PrintsDownload