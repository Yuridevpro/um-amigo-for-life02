# usuarios/utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import threading

class EmailThread(threading.Thread):
    """
    Classe para enviar e-mails em uma thread separada, prevenindo timeouts.
    Inclui logging para depuração em produção.
    """
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.email.send()
            # Log de sucesso (aparecerá nos logs do Render)
            print(f"Email para {self.email.to} enviado com sucesso em segundo plano.")
        except Exception as e:
            # Log de erro (aparecerá nos logs do Render)
            print(f"ERRO ao enviar e-mail em segundo plano para {self.email.to}: {e}")

def enviar_email_com_template(request, subject, template_name, context, recipient_list):
    """
    Renderiza um template HTML e o envia como um e-mail em uma thread separada
    para não bloquear a requisição principal.
    """
    # Adiciona o host (ex: '127.0.0.1:8000' ou 'seu-site.onrender.com') ao contexto
    # para que os links no e-mail sejam gerados corretamente.
    context['host'] = request.get_host()
    
    html_content = render_to_string(template_name, context)
    
    email = EmailMultiAlternatives(
        subject=subject,
        body='', # O corpo principal será o HTML
        from_email=settings.DEFAULT_FROM_EMAIL, # Usa o remetente verificado no SendGrid
        to=recipient_list
    )
    email.attach_alternative(html_content, "text/html")

    # Inicia a thread para enviar o e-mail sem bloquear a aplicação
    EmailThread(email).start()