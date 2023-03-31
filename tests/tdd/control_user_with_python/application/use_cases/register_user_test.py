from abc import ABCMeta, abstractmethod


from control_user_with_python.domain.intefaces.users.register_repo import (
    RegisterUserRepositoryInterface,
)


class RegisterUserInterface(metaclass=ABCMeta):
    """RegisterUserInterface"""

    @abstractmethod
    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        pass


class RegisterUser(RegisterUserInterface):
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

    callsCount: int = 0

    def register(
        self, name: str, email: str, password: str, repeat_password: str
    ):
        """Register"""

        self.name = name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

        self.callsCount += 1


def make_sut():
    """Make SUT"""

    register_user_reposutory = RegisterUserRepositorySpy()
    sut = RegisterUser(register_user_repository=register_user_reposutory)

    return {
        register_user_reposutory: RegisterUserRepositorySpy,
        sut: RegisterUser,
    }


def test_should_be_return_200_when_user_register_sucessfully():
    """Test Register User Successfully"""

    name = "any_name"
    email = "any_email@mail.com"
    password = "any_password"
    repeat_password = "any_password"

    register_user_repository, sut = make_sut()

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
    assert register_user_repository.callsCount == 1
