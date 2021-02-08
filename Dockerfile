FROM python:3

# 設置環境變量
ENV PYTHONUNBUFFERED 1

RUN mkdir /gel_database 

WORKDIR /gel_database

ADD . /gel_database/

RUN pip3 install -r requirements.txt


