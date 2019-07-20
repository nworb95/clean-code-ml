FROM python:3.6-slim

RUN apt-get update \
  && apt-get install -y curl git

RUN git config --global user.email "nworb95@gmail.com"
RUN git config --global user.name "nworb95"

WORKDIR /home/clean-code-ml

COPY . /home/clean-code-ml
RUN pip install -U pip && pip install -r requirements.txt
