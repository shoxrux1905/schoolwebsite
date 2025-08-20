from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def user_login_view(request) :
    """ authentication """
    if request.method == "GET":
        return render(request, 'users/login.html')
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return redirect('login')