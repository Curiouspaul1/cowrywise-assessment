import os

from dotenv import load_dotenv

load_dotenv()


class Base:
    SECRET_KEY = os.getenv('APP_SECRET', str(os.urandom(12)))
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite+pysqlite:///:memory:'
    )


class DevConfig(Base):
    """ Dev environment config go here """
    pass


class TestConfig(Base):
    """ Testing environment config go here """
    pass


class PrdConfig(Base):
    """ Production environment config go here """
    pass


config_options = {
    'default': DevConfig,
    'dev': DevConfig,
    'test': TestConfig
}
