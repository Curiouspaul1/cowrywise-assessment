from marshmallow import fields

from schemas.base import BaseAutoSchema
from models.users import User


class UserSchema(BaseAutoSchema):
    class Meta(BaseAutoSchema.Meta):
        model = User
        load_instance = True


class UserBorrowsSchema(BaseAutoSchema):
    class Meta(BaseAutoSchema.Meta):
        model = User
        include_relationships = True

    borrows = fields.Nested(
        'BorrowSchema',
        many=True,
        exclude=('user', ),
        dump_only=True
    )
