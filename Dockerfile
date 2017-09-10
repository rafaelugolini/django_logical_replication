FROM python:3.6-slim

MAINTAINER Rafael Ugolini "rafael.ugolini@gmail.com"

RUN mkdir /app

WORKDIR /app

RUN apt-get -qq update
RUN apt-get install -y libpq-dev postgresql-client curl

ADD ./requirements.txt /app

RUN pip install -r requirements.txt

ADD ./ /app

ENTRYPOINT ["/app/entrypoint.sh"]
