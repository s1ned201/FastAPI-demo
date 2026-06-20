from datetime import datetime

from pydantic import BaseModel

from src.account.constants import UserSexEnums


class UserCreateSchema(BaseModel):
    fullname: str
    email: str
    sex: UserSexEnums

class UserResponseSchema(BaseModel):
    id: int
    fullname: str
    email: str
    sex: UserSexEnums
    name: str | None = None
    age: int | None = None
    created_at: datetime
    updated_at: datetime