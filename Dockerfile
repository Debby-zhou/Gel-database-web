FROM python:3.6

# 設置環境變量
ENV PYTHONUNBUFFERED 1

RUN mkdir /gel_database 

WORKDIR /gel_database

ADD . /gel_database

RUN apt-get update
RUN apt-get install -y python-pip ython-dev build-essential
COMMAND "python -m  pip install --upgrade pip"
COMMAND "python -m pip install -r requirements.txt"

ENV SPIDER=/gel_database


