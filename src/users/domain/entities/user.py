from dataclasses import dataclass, field
from datetime import datetime, timezone
from users.domain.value_objects.email_address import EmailAddress

@dataclass
class User:
    id: str
    name: str
    email: EmailAddress
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def rename(self, new_name: str) -> None:
        self.name = new_name.strip()
        self.updated_at = datetime.now(timezone.utc)
