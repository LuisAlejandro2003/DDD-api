from dataclasses import dataclass, field
from datetime import datetime, timezone
from users.domain.value_objects.email_address import EmailAddress
from users.domain.exceptions import InvalidUserName

@dataclass
class User:
    id: str
    name: str
    email: EmailAddress
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        n = self.name.strip()
        if not n or len(n) > 100:
            raise InvalidUserName()
        self.name = n

    def rename(self, new_name: str) -> None:
        n = new_name.strip()
        if not n or len(n) > 100:
            raise InvalidUserName()
        self.name = n
        self.updated_at = datetime.now(timezone.utc)
