from typing import Optional, List, Dict
from users.domain.repositories import UserRepository
from users.domain.entities.user import User
from users.domain.value_objects.email_address import EmailAddress

class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self._by_id: Dict[str, User] = {}
        self._by_email: Dict[str, User] = {}

    async def get_by_id(self, user_id: str) -> Optional[User]:
        return self._by_id.get(user_id)

    async def get_by_email(self, email: EmailAddress) -> Optional[User]:
        return self._by_email.get(email.value)

    async def list_all(self) -> List[User]:
        return list(self._by_id.values())

    async def save(self, user: User) -> None:
        self._by_id[user.id] = user
        self._by_email[user.email.value] = user
