from typing import Annotated
from sqlalchemy.orm import Mapped
from src.account.constants import UserSexEnums
from src.core.orm import (
    primary_integer,
    string_64_not_nullable,
    string_64_nullable,
    simple_integer_nullable,
    Base,
    string_64_unique
)


class User(Base):
    __tablename__ = "users"
    id: Mapped[primary_integer]
    name: Mapped[string_64_nullable]
    fullname: Mapped[string_64_not_nullable]
    age: Mapped[simple_integer_nullable]
    sex: Mapped[Annotated[str, UserSexEnums]]
    email: Mapped[string_64_unique]
    password: Mapped[string_64_nullable]

