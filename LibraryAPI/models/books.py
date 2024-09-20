from typing import List
import datetime as dt

from sqlalchemy import (
    select,
    ForeignKey,
    desc
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy.ext.hybrid import hybrid_property

from models.base import Base
from models.datatypes import SerializableEnum
from models.mixins import (
    IdMixin,
    TimestampMixin
)


class BookStatusEnum(SerializableEnum):
    ON_SHELF = 'ON_SHELF'
    BORROWED = 'BORROWED'


class Books(Base, IdMixin, TimestampMixin):
    __tablename__ = 'books'
    book_publisher: Mapped[str] = mapped_column(index=True)
    book_category: Mapped[str] = mapped_column(index=True)
    status: Mapped[BookStatusEnum] = mapped_column(
        default=BookStatusEnum.ON_SHELF
    )
    book_title: Mapped[str] = mapped_column(index=True, unique=True)
    curr_due_date: Mapped[dt.datetime | None]

    # relationships
    borrows: Mapped[List['Borrows']] = relationship(
        back_populates='book',
        cascade='delete'
    )

    # props

    @hybrid_property
    def publisher(self):
        return self.book_publisher

    @hybrid_property
    def category(self):
        return self.book_category

    @hybrid_property
    def title(self):
        return self.book_title

    @publisher.setter
    def publisher(self, data):
        self.book_publisher = data.strip().lower()

    @category.setter
    def category(self, data):
        self.book_category = data.strip().lower()

    @title.setter
    def title(self, data):
        self.book_title = data.strip().lower()

    @classmethod
    def get_by_title(cls, title, session):
        if title and session:
            stmt = select(cls).where(cls.title == title)
            res = session.scalars(stmt).first()
            return res

    @classmethod
    def get_by_publisher(cls, publisher, session):
        if publisher and session:
            stmt = select(cls).where(cls.publisher == publisher)
            return stmt

    @classmethod
    def get_by_category(cls, category, session):
        if category and session:
            category = category.strip()
            stmt = select(cls).where(cls.category == category)
            return stmt


class Borrows(Base, IdMixin, TimestampMixin):
    __tablename__ = 'borrows'
    no_of_days: Mapped[int]
    date_returned: Mapped[dt.datetime | None]

    # foreign keys
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))

    # relationships
    book: Mapped['Books'] = relationship(back_populates='borrows')
    user: Mapped['User'] = relationship(back_populates='borrows')
