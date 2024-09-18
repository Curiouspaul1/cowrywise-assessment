from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from models.base import Base
from models.mixins import IdMixin


class User(Base, IdMixin):
    """ Declarative class based mapping for user table """
    __tablename__ = 'user'
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(unique=True)
