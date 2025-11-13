# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from perfil.models import UserProfile
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import re
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.utils.crypto import get_random_string
from django.utils import timezone
from datetime import timedelta
from .models import Ativacao, ResetSenha
from django.contrib.auth.tokens import default_token_generator
from django.db import transaction

# Importa a nova função de envio de e-mail assíncrono
from .utils import enviar_email_com_template


@transaction.atomic
def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        telefone = request.POST.get('telefone')
        estado_id = request.POST.get('estado_id')
        estado_nome = request.POST.get('estado_nome')
        cidade_nome = request.POST.get('cidade_nome')

        # Validação dos campos
        if not all([nome, sobrenome, email, senha, confirmar_senha, telefone, estado_id, cidade_nome]):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos obrigatórios.')
            return render(request, 'cadastro.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'telefone': telefone, 'estado_id': estado_id, 'cidade_nome': cidade_nome})

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return render(request, 'cadastro.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'telefone': telefone, 'estado_id': estado_id, 'cidade_nome': cidade_nome})

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            messages.add_message(request, constants.ERROR, 'O formato do e-mail é inválido.')
            return render(request, 'cadastro.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'telefone': telefone, 'estado_id': estado_id, 'cidade_nome': cidade_nome})

        senha_pattern = r'^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$'
        if not re.match(senha_pattern, senha):
            messages.add_message(request, constants.ERROR, 'A senha deve conter pelo menos 8 caracteres, incluindo letras e números.')
            return render(request, 'cadastro.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'telefone': telefone, 'estado_id': estado_id, 'cidade_nome': cidade_nome})

        try:
            user_existente = User.objects.filter(email=email).first()
            if user_existente:
                if not user_existente.is_active:
                    # Se o usuário existe mas está inativo, apaga o registro antigo
                    # para permitir um novo cadastro limpo.
                    user_existente.delete()
                else:
                    # Se o usuário já existe e está ativo, informa o erro.
                    messages.error(request, 'Este e-mail já está em uso por uma conta ativa.')
                    return redirect('cadastro')

            # Cria o usuário e o perfil dentro de uma transação atômica
            user = User.objects.create_user(username=email, email=email, password=senha, is_active=False)
            UserProfile.objects.create(
                user=user, telefone=telefone, estado_nome=estado_nome, estado_id=estado_id,
                cidade_nome=cidade_nome, nome=nome, sobrenome=sobrenome, email=email
            )

            # Gera o token de ativação
            token = get_random_string(length=32)
            Ativacao.objects.create(
                user=user,
                confirmation_token=token,
                confirmation_token_expiration=timezone.now() + timedelta(days=1)
            )

            # Prepara o contexto e envia o e-mail usando a nova função
            context = {
                'user': user,
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            }
            enviar_email_com_template(
                request,
                subject='Confirmação de Cadastro - A Friend for Life',
                template_name='email_confirmacao.html',
                context=context,
                recipient_list=[user.email]
            )

            messages.success(request, 'Cadastro realizado com sucesso! Um e-mail de confirmação foi enviado. Por favor, verifique sua caixa de entrada e também a pasta de SPAM.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Ocorreu um erro inesperado durante o cadastro. Nenhuma conta foi criada.')
            # Para depuração, é útil logar o erro
            print(f"Erro de cadastro: {e}")
            return redirect('cadastro')

    return render(request, 'cadastro.html')


def confirmar_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        ativacao = Ativacao.objects.get(user=user, confirmation_token=token)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, Ativacao.DoesNotExist):
        user = None
        ativacao = None

    if user is not None and ativacao is not None and ativacao.confirmation_token_expiration > timezone.now():
        user.is_active = True
        user.save()
        ativacao.delete()
        messages.add_message(request, constants.SUCCESS, 'Email confirmado com sucesso! Você já pode fazer o login.')
        return redirect('login')
    else:
        messages.add_message(request, constants.ERROR, 'Link de confirmação inválido ou expirado. Por favor, tente se cadastrar novamente.')
        return redirect('cadastro')


def logar(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
        
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not email or not senha:
            messages.error(request, 'E-mail e senha são obrigatórios.')
            return redirect('login')

        try:
            # Verifica primeiro se o usuário existe e se está ativo
            user_obj = User.objects.get(email=email)
            if not user_obj.is_active:
                messages.warning(request, 'Sua conta ainda não foi ativada. Verifique seu e-mail de confirmação.')
                return redirect('login')
        except User.DoesNotExist:
            # Se o usuário não existe, a mensagem de erro será tratada pelo 'authenticate'
            pass

        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo(a) de volta!')
            return redirect('/divulgar/novo_pet')
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
            return redirect('login')

    return render(request, 'login.html')


def esqueceu_senha(request):
    if request.method == "POST":
        email_form = request.POST.get('email')
        if not email_form:
            messages.add_message(request, constants.ERROR, 'Por favor, informe um e-mail válido.')
            return render(request, 'esqueceu_senha.html')
        
        try:
            user = User.objects.get(email=email_form)
            
            # Invalida tokens de redefinição anteriores para o mesmo usuário
            ResetSenha.objects.filter(user=user).delete()

            # Cria um novo token
            token = default_token_generator.make_token(user)
            ResetSenha.objects.create(user=user, reset_token=token)

            # Prepara o contexto e envia o e-mail usando a nova função
            context = {
                'user': user,
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            }
            enviar_email_com_template(
                request,
                subject='Redefinição de Senha - A Friend for Life',
                template_name='email_reset_senha.html',
                context=context,
                recipient_list=[user.email]
            )
            
            messages.success(request, 'Um e-mail com instruções para redefinir sua senha foi enviado. Verifique sua caixa de entrada e também a pasta de SPAM.')
            return redirect('login')

        except User.DoesNotExist:
            # Não informa que o usuário não existe por segurança, mas exibe uma mensagem genérica.
            messages.success(request, 'Se houver uma conta associada a este e-mail, um link de redefinição de senha foi enviado.')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.')
            print(f"Erro em esqueceu_senha: {e}")
            return redirect('esqueceu_senha')
    
    return render(request, 'esqueceu_senha.html')


def criar_senha(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode('utf-8')
        user = User.objects.get(pk=uid)
        reset_senha_obj = ResetSenha.objects.get(user=user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ResetSenha.DoesNotExist):
        user = None
        reset_senha_obj = None

    if user is not None and reset_senha_obj is not None and reset_senha_obj.reset_token == token and reset_senha_obj.is_token_valid():
        if request.method == 'POST':
            senha_nova = request.POST.get('senha_nova')
            confirmar_senha = request.POST.get('confirmar_senha')

            if not senha_nova or not confirmar_senha:
                messages.add_message(request, constants.ERROR, 'Ambos os campos de senha são obrigatórios.')
                return render(request, 'criar_senha.html', {'uidb64': uidb64, 'token': token})

            if senha_nova != confirmar_senha:
                messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
                return render(request, 'criar_senha.html', {'uidb64': uidb64, 'token': token})
            
            senha_pattern = r'^(?=.*[a-zA-Z])(?=.*[0-9]).{8,}$'
            if not re.match(senha_pattern, senha_nova):
                messages.add_message(request, constants.ERROR, 'A nova senha deve conter pelo menos 8 caracteres, incluindo letras e números.')
                return render(request, 'criar_senha.html', {'uidb64': uidb64, 'token': token})

            user.set_password(senha_nova)
            user.save()
            reset_senha_obj.delete()
            
            messages.success(request, 'Sua senha foi alterada com sucesso! Faça login com sua nova senha.')
            return redirect('login')
        else:
            return render(request, 'criar_senha.html', {'uidb64': uidb64, 'token': token})
    else:
        messages.error(request, 'O link de redefinição de senha é inválido ou já expirou. Por favor, solicite um novo.')
        return redirect('esqueceu_senha')

@login_required
def sair(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta com sucesso.')
    return redirect('login')

def reenviar_ativacao(request):
    """
    Permite que um usuário com conta inativa solicite um novo e-mail de ativação.
    - Se GET, exibe o formulário para inserir o e-mail.
    - Se POST, verifica se existe um usuário inativo com o e-mail fornecido,
      deleta o token de ativação antigo, cria um novo e o reenvia.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Verifica se a conta já está ativa
            if user.is_active:
                messages.info(request, 'Esta conta já está ativa. Você pode fazer o login.')
                return redirect('login')
            
            # Deleta tokens de ativação antigos para este usuário
            Ativacao.objects.filter(user=user).delete()
            
            # Cria um novo token de ativação
            token = get_random_string(length=32)
            Ativacao.objects.create(
                user=user,
                confirmation_token=token,
                confirmation_token_expiration=timezone.now() + timedelta(days=1)
            )
            
            # Prepara o contexto para o e-mail
            context = {
                'user': user,
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            }

            # Envia o novo e-mail
            enviar_email_com_template(
                request,
                subject='Novo Link de Ativação - A Friend for Life',
                template_name='email_confirmacao.html', # Reutiliza o mesmo template
                context=context,
                recipient_list=[user.email]
            )
            
            messages.success(request, 'Um novo e-mail de ativação foi enviado. Verifique sua caixa de entrada e também a pasta de SPAM.')
            return redirect('login')
            
        except User.DoesNotExist:
            messages.error(request, 'Nenhum usuário inativo encontrado com este e-mail.')
            return redirect('reenviar_ativacao')

    return render(request, 'reenviar_ativacao.html')