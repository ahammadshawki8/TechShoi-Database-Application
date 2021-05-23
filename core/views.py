from django.shortcuts import render
from core.forms import LoginForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "core/index.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('core:index'))
            else:
                return HttpResponse("Account not active!")
        
        else:
            return HttpResponse("Invalid login details supplied!")
    
    else:
        return render(request, 'core/user_login.html', {
            'login_form': LoginForm()
        })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("core:index"))


@login_required
def analytics(request):
    return render(request, "core/analytics.html")