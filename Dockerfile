FROM ubuntu:latest

WORKDIR /spacex

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y postgresql-client
COPY requirements.txt /spacex
RUN python3 -m pip install -r requirements.txt

COPY . /spacex

CMD ["/bin/bash", "start.sh"]
