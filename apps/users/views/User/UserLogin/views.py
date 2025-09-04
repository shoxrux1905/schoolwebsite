from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.views.User.UserLogin.serializer import UserLoginSerializer


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
    
@api_view(['GET'])
def user_login_api_view(request):
    logins = User.objects.all()
    serializer = UserLoginSerializer(logins, many=True)
    return Response(serializer.data)