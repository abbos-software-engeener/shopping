from django.urls import path

from main.views import  ClientLogin

app_name = "main"

urlpatterns = [
    path('login/', ClientLogin.as_view(), name="login"),
]