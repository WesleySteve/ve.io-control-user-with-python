from abc import ABCMeta, abstractmethod


class RegisterUserInterface(metaclass=ABCMeta):
    """RegisterUserInterface"""

    @abstractmethod
    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        pass
