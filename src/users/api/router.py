from fastapi import APIRouter, Depends, status
from users.api.schemas import RegisterUserRequest, UserResponse
from users.application.dtos import RegisterUserInput
from users.application.use_cases.register_user import RegisterUser
from users.api.deps import get_register_user_use_case

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    payload: RegisterUserRequest,
    use_case: RegisterUser = Depends(get_register_user_use_case),
):
    out = await use_case.execute(
        RegisterUserInput(name=payload.name, email=payload.email)
    )
    return UserResponse(id=out.id, name=out.name, email=out.email)