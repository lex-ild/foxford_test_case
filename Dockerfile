FROM python:3.10-alpine3.16

COPY requirements.txt /temp/requirements.txt
RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user
COPY foxford_test_case /foxford_test_case
WORKDIR /foxford_test_case
EXPOSE 8000




USER service-user