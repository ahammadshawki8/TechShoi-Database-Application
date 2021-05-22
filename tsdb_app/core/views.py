from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def analytics(request):
    return render(request, "core/analytics.html")