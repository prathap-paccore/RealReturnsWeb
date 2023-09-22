FROM python:3.12.0rc2-alpine3.18
LABEL maintainer="realreturns.com"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

ARG APPNAME=RealReturnsWeb
ARG APPDIR=/root/${APPNAME}

RUN mkdir ${APPDIR}
WORKDIR ${APPDIR}

ADD . ${APPDIR}

EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip3 install --upgrade pip && \
    apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev && \
    /py/bin/pip3 install -r /requirements.txt && \
    # adduser --disabled-password --no-create-home app
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol 



ENV PATH="/py/bin:$PATH"

# USER app