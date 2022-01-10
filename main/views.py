from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from django.views import View

from .form import LoginForm, CategoryForm
from .models import *


class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(self, request, *args, **kwargs)

        request.title = ("Tizimga kirish")

    def get(self, request):
        return render(request, 'layouts/form.html', {
            'form': LoginForm()
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, phone=form.cleaned_data['phone'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, ("{} Siz tizimga kirdingiz.) ".format(user.username)))

                return redirect('/admin/')

            form.add_error('telefon', "Login va/yoki parrol noto'g'ri!")

        return render(request, 'main/login.html', {
            'form': form
        })


def category_list(request):
    carmodel = Category.objects.all()
    ctx = {
        'carmodel': carmodel,
    }
    return render(request, 'main/category/list.html', ctx)


def category_create(request):
    model = Category()
    form = CategoryForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'main/category/form.html', ctx)