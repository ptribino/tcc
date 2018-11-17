from django import forms
#from django.core.mail import send_mail
from django.conf import settings

#from core.mail import send_mail_template

class ContactItens(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

#FIXME: ajustar para enviar o email ou retirar
#    def send_mail(self):
#        subject = 'Contato sobre o Smartlook'
#        context = {
#            'name': self.celaned_data['name'],
#            'email': self.cleaned_data['email'],
#            'message': self.cleaned_data['message'],
#        }
#        template_name= 'itens/contact_email.html'
#        send_mail_template(
#            subject, template_name, context, [settings.CONTACT_EMAIL]
#        )

