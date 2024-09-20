from typing import Dict

from marshmallow import fields

from schemas.base import BaseAutoSchema
from models.books import (
    Books,
    Borrows
)
from models.datatypes import SerializableEnum


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


class BookActions:

    class ActionEnums(SerializableEnum):
        DELETE = 'DELETE'
        CREATE = 'CREATE'
        MODIFY = 'MODIFY'

    def __init__(self, book_id=None):
        self.book_id = book_id

    def gen_resp(
        self,
        action: ActionEnums,
        data: [None | Dict[any, any]] = None
    ) -> Dict[str, [ActionEnums | int]]:
        """" Generates payload for request to update library db.
            Suggestion or rather possible improvement may be to
            allow specifications for different models. I made it
            work for just <Books> Table since that's the only
            one that needs to be updated in this excercise.
        """
        return {
            'action': action,
            'object_id': self.book_id,
            'data': data
        }

    def delete_book(self):
        return self.gen_resp(
            action=self.ActionEnums.DELETE.value
        )

    def add_book(self, data):
        return self.gen_resp(
            action=self.ActionEnums.CREATE.value,
            data=data
        )

    def edit_book(self):
        return self.gen_resp(action=self.ActionEnums.MODIFY.value)
