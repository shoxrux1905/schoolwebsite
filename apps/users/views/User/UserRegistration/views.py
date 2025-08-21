from django.shortcuts import redirect, render
from apps.users.models import User

def user_student_registration_view(request) :
    """ registration """
    if request.method == "GET":
        return render(request, 'users/registration.html')
    
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    password2 = request.POST["password2"]
    gender = request.POST["gender"]
    phone_number = request.POST["phone_number"]
    address = request.POST["address"]
    date_of_birth = request.POST["date_of_birth"]
    shift = request.POST["shift"]
    study_lang = request.POST["study_lang"]
    blood_group = request.POST["blood_group"]
    pfp = request.FILES.get("pfp")

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
    elif User.objects.filter(email=email).exists() :
        messages = {
            'error': "Bunday elektron pochtali foydalanuvchi tizimda mavjud."
        }
        return render(request, 'users/registration.html', messages)
    elif User.objects.filter(phone_number=phone_number).exists() :
        messages = {
            'error': "Bunday telefon raqamli foydalanuvchi tizimda mavjud."
        }  
        return render(request, 'users/registration.html', messages)
    else :
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            phone_number=phone_number,
            address=address,
            date_of_birth=date_of_birth,
            shift=shift,
            study_lang=study_lang,
            blood_group=blood_group,
            pfp=pfp,
            )
        user.set_password(password)
        user.save()
        return redirect('login')