from django.shortcuts import redirect, render
from apps.users.models import User

def user_registration_view(request) :
    """ registration """
    if request.method == "GET":
        return render(request, 'users/registration.html')
    username = request.POST["username"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    user = User.objects.filter(username=username)
    if user :
        messages = {
            'error': "Bunday usernameli foydalanuvchi tizimda mavjud."
        }
        return render(request, 'users/registration.html', messages)
    elif password != password2 :
        messages = {
            'error': "Parollar mosligini tekshiring."
        }
        return render(request, 'users/registration.html', messages)
    else :
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        messages = {
            'success': "Siz muvaffaqiyatli ro'yxatdan o'tdingiz."
        }
        return redirect('login')