from marshmallow_sqlalchemy import auto_field
from marshmallow import fields

from schemas.base import BaseAutoSchema
from models.books import (
    Books,
    Borrows
)


class BookSchema(BaseAutoSchema):
    class Meta(BaseAutoSchema.Meta):
        model = Books
        load_instance = True
        load_only = ('publisher', 'category',)

    publisher = fields.String(required=True)
    category = fields.String(required=True)

    book_category = fields.String(dump_only=True)
    book_publisher = fields.String(dump_only=True)
    curr_due_date = fields.DateTime(dump_only=True)


class BorrowSchema(BaseAutoSchema):
    class Meta(BaseAutoSchema.Meta):
        model = Borrows
        load_instance = True
        include_fk = True
        include_relationships = True

    book_id = fields.Int(dump_only=True)
    date_returned = fields.Int(dump_only=True)
    book = fields.Nested('BookSchema', dump_only=True, only=(
        'book_title',
        'book_publisher',
        'book_category'
    ))
    user = fields.Nested('UserSchema', dump_only=True)
