from django.urls import path

from apps.users.views import user_login_view, user_login_api_view, user_student_registration_view, user_registration_api_view
from apps.users.views.Home import home_view

urlpatterns = [
    path('login/', user_login_view, name='login'),
    path('login/api/', user_login_api_view, name='login_api'),
    path('home/', home_view, name='home'),
    path('registration/', user_student_registration_view, name='registration'),
    path('registration/api/', user_registration_api_view, name='registration_api'),
]
