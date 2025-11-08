from contextlib import nullcontext
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from  django.views.generic import CreateView
from django.urls import reverse_lazy


# Страница входа с кастомным шаблоном
class CustomLoginView(LoginView):
    template_name = 'leads/auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lead-list')

# Регистрация нового пользователя
class RegisterView(CreateView):
    model = User
    form_class = nullcontext
    template_name = 'leads/auth/register.html'
    success_url = reverse_lazy('lead-list')
