from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from extensions import Session


class BaseAutoSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = Session

    id = fields.Int(dump_only=True)  # read only
    created_at = fields.DateTime(dump_only=True)  # read only
