from django import forms
from django.forms import ModelForm
from django.contrib.auth.hashers import make_password

class formlogin(forms.Form):
    username = forms.CharField(max_length=255)
    password = password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(formlogin, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['placeholder'] = "Ім'я"
        self.fields['password'].widget.attrs['placeholder'] = 'Пороль'
        self.fields['password'].label = ''
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(formlogin, self).save(*args, **kwargs)