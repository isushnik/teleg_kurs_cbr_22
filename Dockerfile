FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN  pip install pyTelegramBotAPI

CMD python /usr/src/app/isushnik_hello.py