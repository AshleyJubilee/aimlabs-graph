from django.shortcuts import render, get_object_or_404

from .models import Username

# Create your views here.
def index(request):
    return render(request, 'home.html',
                  context={
            "session": request.session.get("user"),
        },)

def userpage(request, username):
    username = get_object_or_404(Username, username)
    return render(request, "user.html", {
        "username": username
    })