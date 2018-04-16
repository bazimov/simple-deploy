FROM python:3-slim

WORKDIR /deploy

COPY . /deploy

RUN apt-get update && apt-get install git -y && pip3 install -U .

ENTRYPOINT ["deploy"]

