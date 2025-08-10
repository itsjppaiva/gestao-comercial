from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForm, LoginForm
from .models import Usuario
from django.contrib.auth.hashers import make_password, check_password

def cadastro_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.senha = make_password(form.cleaned_data['senha'])  # hash da senha
            usuario.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login_usuario')
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(senha, usuario.senha):
                    # Armazena o ID do usuário na sessão
                    request.session['usuario_id'] = usuario.id
                    request.session['usuario_nome'] = usuario.nome
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Senha incorreta.')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuário não encontrado.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def dashboard(request):
    usuario_nome = request.session.get('usuario_nome', 'Usuário')
    return render(request, 'usuarios/dashboard.html', {'usuario_nome': usuario_nome})
