# Importing necessary modules & libraries
from django.urls import path
from core import views


# Setting the app_name and url paths
app_name = "core"
urlpatterns = [
    path('', views.index, name="index"),
    path('analytics', views.analytics, name="analytics"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('download_BUF', views.download_BUF, name="download_BUF")
]
