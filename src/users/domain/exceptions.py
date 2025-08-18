class DomainError(Exception):
    default_message = "Domain error"

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)

class EmailAlreadyInUse(DomainError):
    default_message = "Email already in use"

class UserNotFound(DomainError):
    default_message = "User not found"
