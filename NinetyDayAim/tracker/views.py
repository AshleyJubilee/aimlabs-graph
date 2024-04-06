from django.http import HttpResponseRedirect, HttpResponse
from django_htmx.http import HttpResponseClientRedirect
from django.shortcuts import render, redirect
from .forms import UsernameForm
from .api import usernameQuery

def userSearch(request): 
    form = UsernameForm(request.POST)
    if form.is_valid():
        if usernameQuery(form.cleaned_data['userName']) == None:
            return HttpResponse(f'<p>Could not find AimLabs account: {form.cleaned_data['userName']}</p>')
        else:
            return HttpResponseClientRedirect(form.cleaned_data['userName'])


def index(request):

    context = {"form": UsernameForm()}
    return render(request, 'home.html', context)

def userpage(request, username):
    
    context = {"user": username, "form": UsernameForm()}
    return render(request, "user.html", context)

