from django.core.mail import send_mail
from django.conf import settings


def forget_password_email(email,token):
    email_to = [email]
    email_from = settings.EMAIL_HOST_USER
    subject = f'Change Password'
    message =  f"""
    Click The Link To Change Password. http://127.0.0.1:8000/accounts/change_password/{token}/
    """
    send_mail(subject,message,email_from,email_to)