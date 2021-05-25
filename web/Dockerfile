FROM python:3.8-slim

RUN apt-get update

RUN useradd -ms  /bin/bash web

USER web
COPY web /home/web/app
COPY protobufs /home/collector/protobufs

RUN pip3 install pipenv

WORKDIR /home/web/app/web
ENV PATH /home/web/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/web/app/web
