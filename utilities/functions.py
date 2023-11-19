from django.core.mail import send_mail
from django.conf import settings

def send_email(subject, body, email):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=True,
    )
    
    return True
