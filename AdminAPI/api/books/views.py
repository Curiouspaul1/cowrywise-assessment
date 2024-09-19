from flask import (
    request,
    current_app
)
from sqlalchemy import select

from . import books_bp
from extensions import Session
from schemas import (
    BookSchema,
    BorrowSchema
)
from models import Books
from models.books import BookStatusEnum
from AdminAPI.utils import AppResponse
from AdminAPI.api.messages import (
    add_to_msg,
    BOOK_NOT_FOUND,
    INVALID_DATA_FORMAT,
    UNKNOWN_ERROR,
    DELETED_BOOK
)


@books_bp.post('/')
def add_new_book():
    schema = BookSchema()
    payload = request.get_json(force=True)

    with Session() as sess:
        try:
            new_book = schema.load(payload)
            sess.add(new_book)
            sess.commit()
            resp = AppResponse().success(
                data=schema.dump(new_book)
            )
        except Exception as e:
            print(str(e))
            resp = AppResponse().error(
                message=INVALID_DATA_FORMAT,
                data=str(e)
            )
    return resp


@books_bp.delete('/<int:book_id>')
def delete_book(book_id):
    with Session() as sess:
        stmt = select(Books).where(Books.id == book_id)
        book = sess.scalars(stmt).first()

        if not book:
            return AppResponse().error(
                404,
                message=add_to_msg(BOOK_NOT_FOUND, book_id)
            )
        try:
            sess.delete(book)
            sess.commit()
        except Exception as e:
            print(str(e))
            return AppResponse().error(
                500,
                data=str(e),
                message=UNKNOWN_ERROR
            )
    return AppResponse().success(
        message=DELETED_BOOK
    )


@books_bp.get('/unavailable')
def fetch_borrowed_books():
    schema = BookSchema(many=True)

    if 'page' in request.args:
        page = request.args.get('page')
    else:
        page = 1
    PER_PAGE = current_app.config['PAGINATION_LIMIT']

    with Session() as sess:
        stmt = select(Books).where(Books.status == BookStatusEnum.BORROWED)
        borrowed_books = stmt.offset(page).limit(PER_PAGE)
        borrowed_books = sess.scalars(stmt)
        borrowed_books = schema.dump(borrowed_books)

    return AppResponse().success(
        data=borrowed_books
    )
