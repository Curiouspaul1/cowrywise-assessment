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
from LibraryAPI.utils import AppResponse
from LibraryAPI.api.messages import (
    add_to_msg,
    BOOK_NOT_FOUND,
    INVALID_DATA_FORMAT
)


@books_bp.get('/')
def fetch_books():
    schema = BookSchema(many=True)
    if 'page' in request.args:
        page = request.args.get('page')
    else:
        page = 1

    with Session.begin() as sess:
        if 'category' in request.args:
            _cat = request.args.get('category')
            if not isinstance(_cat, str):
                return AppResponse().error(
                    message=f'Invalid type for query param "category"'
                    f'expected "str" got "{type(_cat)}"'
                )
            # search using category
            stmt = Books.get_by_category(_cat, session=sess)
        elif 'publisher' in request.args:
            # search using publisher
            _pub = request.args.get('publisher')
            if not isinstance(_pub, str):
                return AppResponse().error(
                    message=f'Invalid type for query param "category"'
                    f'expected "str" got "{type(_pub)}"'
                )
            stmt = Books.get_by_publisher(_pub, session=sess)
        else:
            stmt = select(Books)

        PER_PAGE = current_app.config['PAGINATION_LIMIT']
        books = stmt.offset(page).limit(PER_PAGE)
        books = sess.scalars(stmt)
        books = schema.dump(books)

    return AppResponse().success(
        data=books
    )


@books_bp.get('/<int:book_id>')
def fetch_book(book_id):
    schema = BookSchema()

    with Session.begin() as sess:
        stmt = select(Books).where(Books.id == book_id)
        book = sess.scalars(stmt).first()

        if book:
            resp = AppResponse().success(
                data=schema.dump(book)
            )
        else:
            resp = AppResponse().error(
                404,
                message=add_to_msg(BOOK_NOT_FOUND, book_id)
            )

    return resp


@books_bp.post('/<int:book_id>/borrow')
def borrow_book_by_id(book_id):
    schema = BorrowSchema()
    payload = request.get_json(force=True)

    with Session() as sess:
        stmt = select(Books).where(Books.id == book_id)
        book = sess.scalars(stmt).first()

        if not book:
            return AppResponse().error(
                404,
                message=add_to_msg(BOOK_NOT_FOUND, book_id)
            )
        try:
            new_borrow = schema.load(payload)
            new_borrow.book_id = book.id
            sess.add(new_borrow)
            sess.commit()
            resp = schema.dump(new_borrow)
        except Exception as e:
            raise e
            print(str(e))
            return AppResponse().error(
                data=str(e),
                message=INVALID_DATA_FORMAT
            )
    return AppResponse().success(
        data=resp
    )
