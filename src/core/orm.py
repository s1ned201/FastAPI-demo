from typing import Optional, Annotated
from sqlalchemy import String
from sqlalchemy.orm import mapped_column


primary_integer = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
string_64_nullable = Annotated[str, mapped_column(String(64), nullable=True)]
simple_string = Annotated[str, Optional]
simple_integer_nullable = Annotated[Optional[int], mapped_column(nullable=True)]