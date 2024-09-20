FROM python:3.12.6-alpine3.20

WORKDIR /huey-worker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN alembic upgrade head

CMD [ "huey_consumer", "huey_worker.huey" , "-w", "2"]