from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Exames
from .models import Exames
# Create your views here.



def homepage(request):
    return render(request = request,
                  template_name='home.html',
                  context = {"exames":Exames.objects.all})


def login_rq(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logado como {username}")
                return redirect('/')
            else:
                messages.error(request, "Senha ou usuário invalido.")
        else:
            messages.error(request, "Senha ou usuário invalido.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
