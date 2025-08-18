from abc import ABC, abstractmethod
from typing import Optional, List
from users.domain.entities.user import User
from users.domain.value_objects.email_address import EmailAddress

class UserRepository(ABC):
    @abstractmethod
    async def get_by_id(self, user_id: str) -> Optional[User]: ...
    @abstractmethod
    async def get_by_email(self, email: EmailAddress) -> Optional[User]: ...
    @abstractmethod
    async def list_all(self) -> List[User]: ...
    @abstractmethod
    async def save(self, user: User) -> None: ...
