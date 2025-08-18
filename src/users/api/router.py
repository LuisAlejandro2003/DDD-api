from fastapi import APIRouter, status
from users.api.schemas import RegisterUserRequest, UserResponse
from users.application.dtos import RegisterUserInput
from users.application.use_cases.register_user import RegisterUser
from users.infrastructure.persistence.user_repository_inmemory import InMemoryUserRepository

repo = InMemoryUserRepository()
register_uc = RegisterUser(repo)

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(payload: RegisterUserRequest):
    out = await register_uc.execute(
        RegisterUserInput(name=payload.name, email=payload.email)
    )
    return UserResponse(id=out.id, name=out.name, email=out.email)
