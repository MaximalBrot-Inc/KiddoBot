# syntax=docker/dockerfile:1.7-labs

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-bookworm



LABEL authors="MaximalBrot Inc."

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/src/app

#RUN  echo 'Acquire::http { Proxy "http://10.5.5.51:3142"; };' >> /etc/apt/apt.conf.d/90proxy

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

#RUN apt-get update

#RUN apt install libopus0 libopus-dev \
#    sudo apt-get install opus-tools
#RUN apt-get install -y --no-install-recommends ffmpeg



COPY  . .

CMD [ "python", "-u", "./KiddoBot.py" ]