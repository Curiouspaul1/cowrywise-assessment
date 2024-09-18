from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from extensions import Session


class BaseAutoSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = Session
