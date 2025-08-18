from dataclasses import dataclass

@dataclass(frozen=True)
class RegisterUserInput:
    name: str
    email: str

@dataclass(frozen=True)
class RegisterUserOutput:
    id: str
    name: str
    email: str
