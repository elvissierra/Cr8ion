from django.shortcuts import render
from django.contrib.auth.models import User, auth
from .models import Prints


    
def index(request):
    return render(request, 'index.html')
def index1(request):
    if request.method=='POST':
        filename= request.POST['filename']
        
        upload1= request.FILES['upload']
        object= Prints.objects.create(filename=filename,upload= upload1)
        object.save()
    context= Prints.objects.all()
    return render(request, 'index1.html', {'context':context})

#class CustomLoginView(LoginView):
#    template_name = 'base/login.html'
#    fields = '__all__'
#   redirect_authenticated_user = True

#class RegisterPage(FormView):
#    template_name= 'base/register.html'
#    form_class = UserCreationForm
#    redirect_authentication_user = True
#    success_url = reverse_lazy ('prints')

