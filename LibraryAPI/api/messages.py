INVALID_DATA_FORMAT = """
    OOps data entry format is invalid, check to make sure 
    that field mappings are accurately represented in the payload
"""
ADDED_NEW_USER = "New user added successfully!"
BOOK_NOT_FOUND = "Book with id '{}' not found"
BORROW_SUCCESS = "Borrow request successful!🔥"


def add_to_msg(msg, data):
    return msg.format(data)
