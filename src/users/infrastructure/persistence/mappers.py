from users.domain.entities.user import User
from users.domain.value_objects.email_address import EmailAddress
from .models import UserModel

def to_entity(row: UserModel) -> User:
    return User(
        id=row.id,
        name=row.name,
        email=EmailAddress(row.email),
        created_at=row.created_at,
        updated_at=row.updated_at,
    )
