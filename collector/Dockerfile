FROM python:3.8-slim

RUN apt-get update

RUN useradd -ms  /bin/bash collector

COPY --chown=collector:collector collector /home/collector/app
COPY --chown=collector:collector protobufs /home/collector/protobufs

USER collector
RUN pip3 install pipenv

WORKDIR /home/collector/app
ENV PATH /home/collector/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/collector/app
