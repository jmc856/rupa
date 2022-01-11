from abc import ABC, abstractmethod

from src.email_.html_parser import HTMLParser
from src.email_.types import EmailAddress


class AbstractEmailClient(ABC):
    """
    Defines interface for sending email to third party clients
    """

    def __init__(self, /, html_parser=None):
        self._html_parser = html_parser or HTMLParser()

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def send(
        self,
        # TODO: Allow for multiple to users
        to: EmailAddress,
        from_: EmailAddress,
        *,
        subject: str = None,
        body: str = None
    ) -> bool:
        ...
