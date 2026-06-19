from typing import Annotated

from sqlalchemy.orm import Mapped, DeclarativeBase

from src.account.constants import UserSexEnums
from src.core.orm import (
    primary_integer,
    string_64_nullable,
    simple_string,
    simple_integer_nullable
)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[primary_integer]
    name: Mapped[string_64_nullable]
    fullname: Mapped[simple_string]
    age: Mapped[simple_integer_nullable]
    sex: Mapped[Annotated[str, UserSexEnums]]
