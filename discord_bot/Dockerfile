FROM python:3.10-slim-buster

# copy requirements, upgrade pip and install requirements.
COPY /requirements.txt /requirements.txt
RUN apt-get update \
  && apt-get -y install gcc
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Set work directory, copy source code to there
WORKDIR /discord_bot
COPY . .