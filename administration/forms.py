from django import forms


class LoginForm(forms.Form):
    email  = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput)