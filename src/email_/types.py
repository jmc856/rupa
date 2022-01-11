from dataclasses import dataclass


@dataclass
class EmailAddress:
    """
    Defines collection of information related to email sender and recipient
    """
    name: str
    address: str
