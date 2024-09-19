import datetime as dt

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class TimestampMixin:
    created_at: Mapped[dt.datetime] = mapped_column(
        default=dt.datetime.utcnow()
    )
