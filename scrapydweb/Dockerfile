ARG BASE_IMAGE_TAG=3.9-slim


FROM python:$BASE_IMAGE_TAG as install-scrapydweb

RUN apt-get update && \
    apt-get install -y --no-install-recommends git

ENV PATH="/opt/venv/bin:$PATH"
RUN python -m venv /opt/venv --upgrade-deps && \
    pip install --no-cache-dir -U git+https://github.com/my8100/scrapydweb.git


FROM python:$BASE_IMAGE_TAG AS run-scrapydweb

RUN apt-get update && \
    apt-get install -y --no-install-recommends telnet && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapydweb /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

COPY ./entrypoint.sh /entrypoint.sh

WORKDIR /app
COPY ./scrapydweb_settings_v*.py .

ARG HTTP_PORT=5000
EXPOSE $HTTP_PORT

CMD ["/entrypoint.sh"]
