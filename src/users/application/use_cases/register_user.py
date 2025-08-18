import uuid
from users.domain.repositories import UserRepository
from users.domain.entities.user import User
from users.domain.value_objects.email_address import EmailAddress
from users.domain.exceptions import EmailAlreadyInUse
from users.application.dtos import RegisterUserInput, RegisterUserOutput

class RegisterUser:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    async def execute(self, data: RegisterUserInput) -> RegisterUserOutput:
        # 1) VO valida/normaliza email
        email_vo = EmailAddress(data.email)

        # 2) Regla de negocio: unicidad de email
        existing = await self.repo.get_by_email(email_vo)
        if existing:
            raise EmailAlreadyInUse()
        
        # 3) Crear entidad de dominio
        new_user = User(
            id=str(uuid.uuid4()),
            name=data.name.strip(),
            email=email_vo,
        )

        # 4) Persistir a través del puerto (repo)
        await self.repo.save(new_user)
        
        # 5) Responder DTO de salida
        return RegisterUserOutput(
            id=new_user.id,
            name=new_user.name,
            email=new_user.email.value,
        )
