from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login     # импортируем для того чтобы запоминать данные юзера и авторизовывать того
from .forms import UserCreationForm # форма для регистрации
from django.views import View


class Register(View):

    template_name = 'registration/register.html'

# передаём ниже форму для создания регистрации, создаём самостоятельно get-request
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    # создаём post-request для создания нового аккаунта User и пишем request вручную

    def post(self, request):
        # передаём данные в форму
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # получаем логин и пароль пользователя.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            # авторизуем пользователя
            login(request, user)
            return redirect('index')

        context = {
            'form': form
        }
        return render(request, self.template_name, context)
