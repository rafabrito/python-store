from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string

class EnviarEmail():

    def enviar_email_confirmacao_novo_cliente(self, email_cliente,purl):

        link = 'http://127.0.0.1:8000/main/confirmar_email?purl=' + purl;

        html = '<p>Seja bem-vindo a nossa loja PYTHONSTORE.</p>'
        html += '<p>Para poder entrar na nossa loja necessita confirmar o seu email.</p>'
        html += '<p>Para confirmar o email, clique no link abaixo:</p>'
        html += '<p><a href="' + link + '">Confirmar Email</a></p>'
        html += '<p><i><small>PYTHONSTORE</small></i></p>'
        
        content = 'Seja bem-vindo a nossa loja PYTHONSTORE.'
        content += 'Para poder entrar na nossa loja necessita confirmar o seu email.'
        content += 'Para confirmar o email, clique no link abaixo:'
        content += 'Confirmar Email'
        content += 'PYTHONSTORE'


        send_mail(
            subject="PYTHONSTORE - Confirmação de email.",
            message=content,
            from_email="no-replay@pythonstore.com",
            recipient_list=[email_cliente],
            html_message=html
        )

        

    