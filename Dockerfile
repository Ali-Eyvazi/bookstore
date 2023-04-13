FROM python:slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /home
COPY  ./bookstore .




RUN pip install --upgrade pip && \
    pip install -r requirements.txt

 WORKDIR /home/bookstore/


