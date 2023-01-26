FROM python:3.8.10

RUN mkdir -p /usr/source/app
COPY . /usr/source/app
WORKDIR /usr/source/app

RUN pip install -r requirements.txt

EXPOSE 8000
