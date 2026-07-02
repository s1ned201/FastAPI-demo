from sqlalchemy.orm import Session
from src.account.models import User
from src.account.repositories.user import UserRepository
from src.account.schemas.user import UserCreateSchema


class UserAlreadyExist(Exception):
    pass

class UserNotfound(Exception):
    pass

class UserService:
    def __init__(self, session: Session):
        self.session = session
        self.repository = UserRepository(session=session)

    def check_exist(self, email: str = None, user_id: int = None) -> bool:
        if email:
            return bool(self.repository.check_exists_email(email=email))
        if user_id:
            return bool(self.repository.check_exists_user_id(user_id=user_id))
        return False

    def create(self, user_schema: UserCreateSchema) -> User:
        if self.check_exist(email=user_schema.email):
            raise UserAlreadyExist
        return self.repository.create(user_schema=user_schema)

    def get_one(self, user_id: int) -> User:
        if self.check_exist(user_id=user_id):
            return self.repository.get_one(user_id=user_id)
        raise UserNotfound

    def get_all(self) -> list[User]:
        return list(self.repository.get_all())

    def update(self, user_id: int, user_schema: UserCreateSchema) -> User:
        user = self.get_one(user_id=user_id)
        return self.repository.update(user= user, user_schema=user_schema)

    def delete(self, user_id: int) -> None:
        user = self.get_one(user_id=user_id)
        return self.repository.delete(user= user)

