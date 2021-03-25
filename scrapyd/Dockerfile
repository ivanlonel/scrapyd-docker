ARG BASE_IMAGE_TAG=3.9-slim


FROM python:$BASE_IMAGE_TAG as install-scrapyd

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git

RUN curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion -o /tmp/scrapy_bash_completion

ENV PATH="/opt/venv/bin:$PATH"
RUN python -m venv /opt/venv --upgrade-deps && \
    pip install --no-cache-dir -U \
        git+https://github.com/scrapy/scrapyd.git \
        botocore \
        bs4 \
        cloudscraper


FROM python:$BASE_IMAGE_TAG AS run-scrapyd

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapyd /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

COPY --from=install-scrapyd /tmp/scrapy_bash_completion /etc/bash_completion.d/scrapy_bash_completion
RUN echo 'source /etc/bash_completion.d/scrapy_bash_completion' >> /root/.bashrc

COPY ./entrypoint.sh /entrypoint.sh
COPY ./generate_conf.py /tmp/generate_conf.py

ARG HTTP_PORT=6800
EXPOSE $HTTP_PORT

CMD ["/entrypoint.sh"]
