import json
from unittest import mock, TestCase

from app import app


class TestApi(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_calls_send_email_operation(self):
        payload = json.dumps({
            "to": "innocent.person@gmail.com",
            "to_name": "Innocent web surfer",
            "from": "some.absurdly.fake.email@randomletters.com",
            "from_name": "Definitely not a hacker",
            "subject": "Subject that appears very real",
            "body": "<script>JS Injection Attempt</script>"
        })

        with mock.patch('app.send_email_operation') as mock_send_email:
            mock_send_email.return_value = True, 'mock-email-client'
            response = self.app.post('/email',  headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(200, response.status_code)
        self.assertEqual({'client_used': 'mock-email-client', 'sent': True}, response.json)

        mock_send_email.assert_called_once_with(
            "innocent.person@gmail.com",
            "Innocent web surfer",
            "some.absurdly.fake.email@randomletters.com",
            "Definitely not a hacker",
            "Subject that appears very real",
            "<script>JS Injection Attempt</script>"
        )

    def test_fails_to_send_email(self):
        pass

    def test_missing_params_returns_400(self):
        payload = json.dumps({
            "to": "j.calvert55@gmail.com",
            "from": "j.calvert55@gmail.com",
            "from_name": "Ms. Fake",
        })

        response = self.app.post('/email',  headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(400, response.status_code)

    def test_bad_params_returns_400(self):
        payload = json.dumps({
            "to": "innocent.person@gmail.com",
            "to_name": "Innocent web surfer",
            "from": "some.absurdly.fake.email@randomletters.com",
            "from_name": 123,
            "subject": "Subject that appears very real",
            "body": "<script>JS Injection Attempt</script>"
        })

        response = self.app.post('/email',  headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(400, response.status_code)

