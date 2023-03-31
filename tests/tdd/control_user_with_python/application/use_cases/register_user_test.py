from abc import ABCMeta, abstractmethod


class RegisterUserRepositoryInterface(metaclass=ABCMeta):
    """RegisterUserRepositoryInterface"""

    @abstractmethod
    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        """Register"""
        pass


class RegisterUser:
    """RegisterUser"""

    def __init__(
        self, register_user_repository: RegisterUserRepositoryInterface
    ) -> None:
        """Init RegisterUser"""

        self.register_user_repository = register_user_repository

    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        self.register_user_repository.register(
            name=name,
            email=email,
            password=password,
            repeat_password=repeat_password,
        )


class RegisterUserRepositorySpy(RegisterUserRepositoryInterface):
    """RegisterUserRepositorySpy"""

    name: str
    email: str
    password: str
    repeat_password: str

    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        """Register"""

        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password


def test_should_be_return_200_when_user_register_sucessfully():
    """Test Register User Successfully"""

    name = "any_name"
    email = "any_email@mail.com"
    password = "any_password"
    repeat_password = "any_password"

    register_user_repository = RegisterUserRepositorySpy()

    sut = RegisterUser(register_user_repository)

    sut.register(
        name=name,
        email=email,
        password=password,
        repeat_password=repeat_password,
    )

    assert register_user_repository.name == name
    assert register_user_repository.email == email
    assert register_user_repository.password == password
    assert register_user_repository.repeat_password == repeat_password
