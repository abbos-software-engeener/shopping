from dataclasses import fields

from django import forms

from main.models import Category


class LoginForm(forms.Form):
    phone = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'