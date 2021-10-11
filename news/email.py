
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import os
from dotenv import load_dotenv

load_dotenv()


def send_welcome_email(name, recipient):
    # Creating message subject and sender
    subject = 'Welcome to Zoo Tribune!'
    sender = os.environ.get('EMAIL_HOST_USER')

    # Passing context variables
    text_content = render_to_string('email/newsemail.txt', {"name": name})
    html_content = render_to_string('email/newsemail.html', {"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [recipient])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

