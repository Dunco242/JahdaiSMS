from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("index")  # Assuming you have an 'index' view in your app
            else:
                msg = 'Invalid username or password!'
        else:
            msg = 'An error occurred.'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout_view(request):
    logout(request)
    return redirect(reverse("login"))  # Redirect to the desired page after logout
