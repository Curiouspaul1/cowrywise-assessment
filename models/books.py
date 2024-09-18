from sqlalchemy.orm import (
    Mapped,
    mapped_column
)
from sqlalchemy.ext.hybrid import hybrid_property

from models.base import Base
from models.mixins import (
    IdMixin,
    TimestampMixin
)


class Books(Base, IdMixin, TimestampMixin):
    __tablename__ = 'books'
    book_publisher: Mapped[str] = mapped_column(index=True)
    book_category: Mapped[str] = mapped_column(index=True)
    title: Mapped[str]

    @hybrid_property
    def publisher(self):
        return self.book_publisher

    @hybrid_property
    def category(self):
        return self.book_category

    @publisher.setter
    def publisher(self, data):
        self.book_publisher = data.strip().lower()

    @category.setter
    def category(self, data):
        self.book_category = data.strip().lower()

    @classmethod
    def get_by_title(cls):
        pass
