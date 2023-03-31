from control_user_with_python.domain.use_cases.users.register import (
    RegisterUserInterface,
)
from control_user_with_python.domain.intefaces.users.register_repo import (
    RegisterUserRepositoryInterface,
)


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
