from pydantic import BaseModel, EmailStr, Field

class RegisterUserRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
