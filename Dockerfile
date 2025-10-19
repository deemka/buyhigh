FROM python:3.14-trixie

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y \
    pipenv

ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ARG uid=1000
ARG gid=1000
RUN groupadd -g $gid buyhigh && useradd -lm -u $uid -g $gid buyhigh

USER buyhigh

ENV PATH="/home/buyhigh/.local/bin:${PATH}"
RUN pip install -U pip

WORKDIR /app
COPY Pipfile* /app
RUN pipenv install

COPY . /app
WORKDIR /app
