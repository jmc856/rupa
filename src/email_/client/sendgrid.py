import logging
import os
import requests

from .base import AbstractEmailClient

logger = logging.getLogger(__name__)
logger.debug = print  # Replace with real flask logging


class SendGridEmailClient(AbstractEmailClient):
    """
    SendGrid implementation of AbstractEmailClient.
    Sends email via SendGrid API.

    NOTE: Utilizes SendGrid single sender feature
    """

    url = 'https://api.sendgrid.com/v3/mail/send'

    @property
    def api_key(self):
        return os.environ.get('SENDGRID_API_KEY')

    @property
    def headers(self):
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    @property
    def name(self):
        return 'SendGrid'

    def send(self, to, from_, subject=None, body=None) -> bool:
        response = requests.post(
            url=self.url,
            headers=self.headers,
            json={
                'personalizations': [
                    {
                        'to': [{'email': to.address, 'name': to.name}],
                        'subject': subject,
                    }
                ],
                'content': [{"type": "text/plain", "value": self._html_parser.parse(body)}],
                'from': {"email": from_.address, "name": from_.name},
                'reply_to': {"email": from_.address, "name": from_.name}
            }
        )

        # TODO: Add more nuanced error handling
        sent = 202 >= response.status_code >= 200

        if sent is False:
            logger.debug(
                f'Failed to send email to sendgrid API with status_code {response.status_code} and text {response.text}'
            )

        return sent
