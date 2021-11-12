from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.views import generic

# Create your views here.

class Home(generic.TemplateView):
    template_name = 'home.html'

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if (user is not None):
            login(request, user)
            return redirect('home') 
        
        return render(request, 'login.html',{'error': 'Credenciales incorrectas, vuelta a intentarlo'})
    
    return render(request, 'login.html')

def register_view(request):
    
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')