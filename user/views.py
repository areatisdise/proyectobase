from django.shortcuts import render
from allauth.account.views import SignupView, LoginView
from user.forms import RegisterForm, LoginForm
from .models import User  # o desde .models import TuModelo
from django.contrib import messages
from django.db import IntegrityError

class CustomSignupView(SignupView):
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form_class = RegisterForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

def test(request):
    form = RegisterForm()

    # Suponiendo que User es tu modelo de usuario
    user = User.objects.get(id=1)
    print("User object:", user)

    # Envía un mensaje de éxito
    messages.success(request, '¡Este es un mensaje de éxito de prueba!')

    return render(request, 'users/test.html', {'form': form, 'user': user})

