from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from users.domain.exceptions import (
    EmailAlreadyInUse,
    UserNotFound,
    DomainError,
    InvalidEmail,
    InvalidUserName,
)

def register_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(EmailAlreadyInUse)
    async def email_conflict_handler(request: Request, exc: EmailAlreadyInUse):
        return JSONResponse(
            status_code=409,
            content={"detail": str(exc), "error": "email_conflict"},
        )

    @app.exception_handler(UserNotFound)
    async def user_not_found_handler(request: Request, exc: UserNotFound):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc), "error": "user_not_found"},
        )

    @app.exception_handler(InvalidEmail)
    async def invalid_email_handler(request: Request, exc: InvalidEmail):
        return JSONResponse(
            status_code=422,
            content={"detail": str(exc), "error": "invalid_email"},
        )

    @app.exception_handler(InvalidUserName)
    async def invalid_user_name_handler(request: Request, exc: InvalidUserName):
        return JSONResponse(
            status_code=422,
            content={"detail": str(exc), "error": "invalid_user_name"},
        )

    # Fallback para otros errores de dominio
    @app.exception_handler(DomainError)
    async def domain_error_handler(request: Request, exc: DomainError):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc), "error": "domain_error"},
        )
