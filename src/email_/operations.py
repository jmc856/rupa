from .factories import get_default_email_client
from .types import EmailAddress


def send_email(to: str, to_name: str, from_: str, from_name: str, subject: str, body: str) -> tuple[bool, str]:
    client = get_default_email_client()
    sent = client.send(
        EmailAddress(address=to, name=to_name),
        EmailAddress(address=from_, name=from_name),
        subject=subject,
        body=body
    )

    return sent, client.name
