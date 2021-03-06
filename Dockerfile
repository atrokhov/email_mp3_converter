FROM python:2.7.10
LABEL maintainer="Arthur Atrokhov <aatrokhov@gmail.com>"
ENV DJANGO_SETTINGS_MODULE email_mp3_converter.settings
RUN pip install --upgrade pip
ADD requirements.txt /email_mp3_converter/requirements.txt
RUN pip install -r /email_mp3_converter/requirements.txt
ADD . /email_mp3_converter
WORKDIR /email_mp3_converter/
RUN adduser --disabled-password --gecos '' myuser