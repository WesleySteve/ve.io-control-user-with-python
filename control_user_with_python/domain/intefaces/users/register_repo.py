from abc import ABCMeta, abstractmethod


class RegisterUserRepositoryInterface(metaclass=ABCMeta):
    """RegisterUserRepositoryInterface"""

    @abstractmethod
    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        """Register"""
        pass
