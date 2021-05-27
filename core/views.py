# Importing necessary modules & libraries
from django.shortcuts import render
from core.forms import LoginForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core import backup
from core import analytics as module_analytics



# Creating Django Views.
# Each URL Paths will be connected to a Django View and 
# Each Django View will be connected to a html file
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
                return render(request, 'core/login_error.html', {"headline": "Account Not Active!"})
        
        else:
            return render(request, 'core/login_error.html', {"headline": "Invalid Login Details Supplied!"})
    
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
    module_analytics.main()
    return render(request, "core/analytics.html")


@login_required
def download_BUF(request):
    zip_file = open("BUF.zip", "rb")
    response = HttpResponse(zip_file, content_type="application/force-download")
    response["Content-Disposition"] = f"attachment; filename=BUF.zip"
    return response