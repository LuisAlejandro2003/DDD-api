from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from users.domain.exceptions import (
    EmailAlreadyInUse,
    UserNotFound,
    DomainError,
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

    # Fallback para otros errores de dominio
    @app.exception_handler(DomainError)
    async def domain_error_handler(request: Request, exc: DomainError):
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc), "error": "domain_error"},
        )
