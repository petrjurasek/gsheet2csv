FROM python:3.5-slim
MAINTAINER Petr Jurasek

RUN pip install pipenv

COPY . /app
WORKDIR /app

RUN pipenv lock -r > requirements.txt && pip install -r requirements.txt --target vendor

COPY docker-entrypoint.sh /usr/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]
