from django import forms
from django.http import HttpResponseRedirect

class UsernameForm(forms.Form):
    userName = forms.CharField(label="Aimlabs Username", max_length=50)

