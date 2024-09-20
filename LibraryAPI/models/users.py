from typing import List

from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from models.base import Base
from models.mixins import (
    IdMixin,
    TimestampMixin
)


class User(Base, IdMixin, TimestampMixin):
    """ Declarative class based mapping for user table """
    __tablename__ = 'user'
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(unique=True)

    # relationships
    borrows: Mapped[List["Borrows"]] = relationship(back_populates='user')
