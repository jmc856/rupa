import logging
import os
import requests

from .base import AbstractEmailClient

logger = logging.getLogger(__name__)
logger.debug = print  # Replace with real flask logging


class MailGunEmailClient(AbstractEmailClient):
    """
    MailGun implementation of AbstractEmailClient.
    Sends email via MailGun API.

    NOTE: When using mailgun sandbox domain, will only forward an email to an explicitly verified address
    """

    @property
    def auth(self):
        return 'api', os.environ.get('MAILGUN_API_KEY')

    @property
    def url(self):
        return f'https://api.mailgun.net/v3/{os.environ.get("MAILGUN_DOMAIN")}/messages'

    @property
    def name(self):
        return 'Mailgun'

    def send(self, to, from_, subject=None, body=None) -> bool:
        data = {
            'from': f'{from_.name} <{from_.address}>',
            'to': f'{to.name} <{to.address}>',
            'subject': subject,
            'text': self._html_parser.parse(body),
        }

        response = requests.post(
            url=self.url,
            data=data,
            auth=self.auth,
        )
        # TODO: Add more nuanced error handling
        sent = 202 >= response.status_code >= 200
        if sent is False:
            logger.debug(
                f'Failed to send email to mailgun API with status_code {response.status_code} and text {response.text}'
            )

        return sent
