from dataclasses import dataclass
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self):
        v = self.value.strip().lower()
        if not _EMAIL_RE.match(v):
            raise ValueError("Invalid email format")
        object.__setattr__(self, "value", v)