from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


def init_ext(app):
    engine = create_engine(
        app.config['SQLALCHEMY_DATABASE_URI']
    )
    Session.configure(bind=engine)
    app.config['DB_ENGINE'] = engine
