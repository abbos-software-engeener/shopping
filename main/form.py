from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,  required=True)
    phone = forms.IntegerField(max_length=50, widget=forms.PasswordInput, label=("phone"), required=True)