from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBEngine:
    def __init__(self, app: Flask = None):
        self.app = app
        self.session = sessionmaker()

    def init_app(self, app):
        self.app = app
        engine = create_engine(
            app.config['SQLALCHEMY_DATABASE_URI']
        )
        self.session.configure(bind=engine)
