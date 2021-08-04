from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.views.generic.list import ListView
from .models import Prints

def index(request):
    return render(request, 'base/index.html')
def index1(request):
    if request.method=='POST':
        filename= request.POST['filename']
        upload1= request.FILES['upload']
        object= Prints.objects.create(title=filename,upload= upload1)
        object.save()
    context= Prints.objects.all()
    return render(request, 'base/index.html', {'context':context})


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