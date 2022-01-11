import os
from unittest import mock, TestCase

from src.email_.client.mailgun import MailGunEmailClient
from src.email_.types import EmailAddress


class TestMailGunClient(TestCase):

    def setUp(self):
        self.mock_html_parser = mock.Mock()
        self.client = MailGunEmailClient(html_parser=self.mock_html_parser)

        # Patch requests package
        mock_requests_patcher = mock.patch('src.email_.client.mailgun.requests')
        self.mock_requests = mock_requests_patcher.start()
        self.addCleanup(mock_requests_patcher.stop)

    @mock.patch.dict(os.environ, {"MAILGUN_DOMAIN": "mock-domain", "MAILGUN_API_KEY": "mock-api-key"})
    def test_send_makes_correct_http_request(self):
        self.mock_html_parser.parse.return_value = 'parsed body'
        mock_response = mock.Mock(status_code=202)
        self.mock_requests.post.return_value = mock_response

        self.client.send(
            EmailAddress('To Name', 'To Address'),
            EmailAddress('From Name', 'From Address'),
            'subject',
            'body'
        )

        self.mock_requests.post.assert_called_once_with(
            url='https://api.mailgun.net/v3/mock-domain/messages',
            data={
                'from': 'From Name <From Address>',
                'to': 'To Name <To Address>',
                'subject': 'subject',
                'text': 'parsed body'
            },
            auth=('api', 'mock-api-key')
        )

        self.mock_html_parser.parse.assert_called_once_with('body')
