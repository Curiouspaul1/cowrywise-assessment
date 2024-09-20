INVALID_DATA_FORMAT = """
    OOps data entry format is invalid, check to make sure 
    that field mappings are accurately represented in the payload
"""
ADDED_NEW_USER = "New user added successfully!"
BOOK_NOT_FOUND = "Book with id '{}' not found"
BORROW_SUCCESS = "Borrow request successful!🔥"
UNKNOWN_ERROR = "OOps an internal server issue occured."
DELETED_BOOK = "Book removed from catalogue"
BOOK_BORROWED = "Book has been borrowed by another user"


def add_to_msg(msg, data):
    return msg.format(data)
