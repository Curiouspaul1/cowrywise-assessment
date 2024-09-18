from schemas.base import BaseAutoSchema
from models.users import User


class UserSchema(BaseAutoSchema):
    class Meta(BaseAutoSchema.Meta):
        model = User
        load_instance = True
