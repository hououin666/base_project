from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from core.models.base import Base


class User(Base):
    username: Mapped[str]
    password: Mapped[str]