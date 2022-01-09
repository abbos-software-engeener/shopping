from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .form import LoginForm


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
            user = authenticate(request, username=form.cleaned_data['username'], phone=form.cleaned_data['phone'])
            if user is not None:
                login(request, user)

                messages.success(request, ("{} Siz tizimga kirdingiz.) ".format(user.username)))

                return redirect('main:index')

            form.add_error('telefon', "Login va/yoki parrol noto'g'ri!")

        return render(request, 'main/login.html', {
            'form': form
        })
