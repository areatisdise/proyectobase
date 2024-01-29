from django.contrib import messages
from django.db import IntegrityError
from django import forms
from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import User

class RegisterForm(SignupForm):
    DniUsu = forms.CharField(max_length=8, required=True, label='DNI')

    class Meta:
        model = User
        fields = ['username', 'password', 'DniUsu']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarse'))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        DniUsu = cleaned_data.get('DniUsu')

        if User.objects.filter(DniUsu=DniUsu).exists():
            raise forms.ValidationError('El DNI ya está en uso. Por favor, elige otro.')

    def save(self, request):
        # Validamos la unicidad del DNI antes de intentar guardar al usuario
        user = super(RegisterForm, self).save(request)
        user.DniUsu = self.cleaned_data['DniUsu']
        user.save()
        return user

class LoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        # Obtén el widget del campo remember y ajusta los atributos
        remember_widget = self.fields['remember'].widget
        remember_widget.attrs['class'] = 'form-check-input'
        remember_widget.attrs['style'] = 'margin-left: 0;'  # Ajusta este valor según sea necesario

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Iniciar sesión'))
