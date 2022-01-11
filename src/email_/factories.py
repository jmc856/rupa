import os

from .client.mailgun import MailGunEmailClient
from .client.sendgrid import SendGridEmailClient


# TODO: Cache the classes
def get_default_email_client():
    client = {
        'mailgun': MailGunEmailClient,
        'sendgrid': SendGridEmailClient,
    }.get(os.environ.get('EMAIL_CLIENT')) or MailGunEmailClient

    return client()
