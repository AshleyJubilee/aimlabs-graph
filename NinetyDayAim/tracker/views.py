from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import UsernameForm


def index(request):
    # Username Search
    if request.method == "POST":
        form = UsernameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(form.cleaned_data['userName'])
    else:
        form = UsernameForm()

    return render(request, 'home.html', {"form": form})

def userpage(request, username):
    # Username Search
    if request.method == "POST":
        form = UsernameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(form.cleaned_data['userName'])
    else:
        form = UsernameForm()

    return render(request, "user.html", {"user": username, "form": form})

