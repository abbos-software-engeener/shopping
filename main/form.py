from django import forms


class LoginForm(forms.Form):
    phone = forms.CharField(required=True)
    password = forms.IntegerField(widget=forms.PasswordInput, required=True)