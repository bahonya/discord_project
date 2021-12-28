FROM python:3.8.1-alpine
WORKDIR /discord_bot

# install system dependencies
RUN yum -y update
# copy requirements, upgrade pip and install requirements.
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /discord_bot
CMD python3 bot.py