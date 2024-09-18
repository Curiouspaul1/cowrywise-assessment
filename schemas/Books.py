from marshmallow_sqlalchemy import auto_field
from marshmallow import fields

from schemas.base import BaseAutoSchema
from models.books import Books


class BookSchema(BaseAutoSchema):
    class Meta:
        model = Books
        load_instance = True

    publisher = fields.String(required=True)
    category = fields.String(required=True)
