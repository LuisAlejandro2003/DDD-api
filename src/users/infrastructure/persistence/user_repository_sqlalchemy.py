from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from users.domain.repositories import UserRepository
from users.domain.entities.user import User
from users.domain.value_objects.email_address import EmailAddress
from users.domain.exceptions import EmailAlreadyInUse
from .models import UserModel
from .mappers import to_entity

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, user_id: str) -> Optional[User]:
        res = await self.session.execute(select(UserModel).where(UserModel.id == user_id))
        row = res.scalar_one_or_none()
        return to_entity(row) if row else None

    async def get_by_email(self, email: EmailAddress) -> Optional[User]:
        res = await self.session.execute(select(UserModel).where(UserModel.email == email.value))
        row = res.scalar_one_or_none()
        return to_entity(row) if row else None

    async def list_all(self) -> List[User]:
        res = await self.session.execute(select(UserModel))
        rows = res.scalars().all()
        return [to_entity(r) for r in rows]

    async def save(self, user: User) -> None:
        # Upsert sencillo por id
        res = await self.session.execute(select(UserModel).where(UserModel.id == user.id))
        row = res.scalar_one_or_none()
        if row is None:
            row = UserModel(
                id=user.id,
                name=user.name,
                email=user.email.value,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            self.session.add(row)
        else:
            row.name = user.name
            row.email = user.email.value
            row.updated_at = user.updated_at

        try:
            await self.session.commit()
        except IntegrityError as e:
            # índice único de email violado, o similar
            await self.session.rollback()
            raise EmailAlreadyInUse() from e
