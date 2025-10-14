# src/identity/users/api/deps.py
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.db.session import get_session
from users.domain.repositories import UserRepository
from users.infrastructure.persistence.user_repository_sqlalchemy import SQLAlchemyUserRepository
from users.infrastructure.persistence.user_repository_sqlalchemy import SQLAlchemyUserRepository
from users.application.use_cases.register_user import RegisterUser

def get_user_repository(session: AsyncSession = Depends(get_session)) -> UserRepository:
    return SQLAlchemyUserRepository(session)  

def get_register_user_use_case(
    repo: UserRepository = Depends(get_user_repository),
) -> RegisterUser:
    return RegisterUser(repo)