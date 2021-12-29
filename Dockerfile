FROM python:3.8.5-alpine

COPY ./app /app
WORKDIR /app

RUN set -ex \
    && apk add --virtual .build-deps gcc linux-headers musl-dev \
    && pip install -r /app/requirements.txt \
    && chmod +x /app/run.sh \
    && apk del gcc \
    && rm -rf ~/.cache /var/cache/

ENTRYPOINT ["/app/run.sh"]