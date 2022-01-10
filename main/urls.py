from django.urls import path

from main.views import *

app_name = "main"

urlpatterns = [
    path('login/', ClientLogin.as_view(), name="login"),
    path('category_list/', category_list, name="category_list"),
    path('category_create/', category_create, name="category_create"),
]