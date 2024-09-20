from sqlalchemy import select

from schemas import BookSchema
from models import Books
from extensions import Session


def add_book(incoming):
    data = incoming['data']
    schema = BookSchema()
    with Session.begin() as sess:
        new_book = schema.load(data)
        sess.add(new_book)


def delete_book(incoming):
    _id = incoming['object_id']
    with Session.begin() as sess:
        stmt = select(Books).where(Books.id == _id)
        book = sess.scalars(stmt).first()

        sess.delete(book)


sync_actions = {
    'CREATE': add_book,
    'DELETE': delete_book
}
