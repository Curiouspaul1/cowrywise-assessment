import enum


class SerializableEnum(str, enum.Enum):
    """ Makes for a JSON serializable enum """
    pass
