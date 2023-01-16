from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError


def cadastro(request):
    if request.user.is_authenticated:
        # if user is already logged in, redirect to home
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        # check if any field is empty
        if not all([nome, email, senha, confirmar_senha]):
            messages.error(request, 'Por favor preencha todos os campos')
            return render(request, 'cadastro.html')
        # check if password and confirmation are different
        if senha != confirmar_senha:
            messages.error(request, 'Senhas não conferem')
            return render(request, 'cadastro.html')
        # check if email already in use
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Esse email já está em uso')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            # hashing password
            user.set_password(senha)
            user.save()
            messages.success(request, 'Usuário criado com sucesso')
            return render(request, 'login.html')

        except IntegrityError:
            messages.error(request, 'Esse email já está em uso')
            return render(request, 'cadastro.html')


def logar(request):
    if request.user.is_authenticated:
        # if user is already logged in, redirect to home
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(request, username=nome, password=senha)
        # check if email and senha exists
        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.error(request, 'Email ou senha inválidos')
            return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('/auth/login')