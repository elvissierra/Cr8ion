from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Prints


class PrintsList(ListView):
    model = Prints
    context_object_name = 'print'
    template_name = 'base/prints_list.html'
    
#class CustomLoginView(LoginView):
#    template_name = 'base/login.html'
#    fields = '__all__'
#   redirect_authenticated_user = True

#class RegisterPage(FormView):
#    template_name= 'base/register.html'
#    form_class = UserCreationForm
#    redirect_authentication_user = True
#    success_url = reverse_lazy ('prints')

 #   def form_valid(self, form):
 #       user = form.save()
 #       if user != None:
 #           login(self.request, user)
 #       return super(RegisterPage, self).form_valid(form)

#    def get(self, args, kwargs):
#        if self.request.user.is_authenticated:
#            return redirect('prints')
#        return super(RegisterPage, self).get(args, kwargs)



#class PrintsUpload

#class PrintsDownload