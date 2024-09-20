import os
from typing import Dict

from huey import RedisHuey
from dotenv import load_dotenv

from utils import send_request

load_dotenv()

huey = RedisHuey(
    host=os.getenv('REDIS_HOST'),
    password=os.getenv('REDIS_PASS')
)


@huey.task()
def update_library(data: Dict) -> None:
    _path = 'api/wbhook'
    print('running..')
    send_request(_path, data)
    print('done..')

# from huey.serializer
