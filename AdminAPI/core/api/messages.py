INVALID_DATA_FORMAT = """
    OOps data entry format is invalid, check to make sure 
    that field mappings are accurately represented in the payload
"""
BOOK_NOT_FOUND = "Book with id '{}' not found"
UNKNOWN_ERROR = "OOps an internal server issue occured."
DELETED_BOOK = "Book removed from catalogue"


def add_to_msg(msg, data):
    return msg.format(data)
