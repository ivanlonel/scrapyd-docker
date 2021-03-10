ARG BASE_IMAGE_TAG=3.9-slim
ARG HTTP_PORT=6800


FROM python:$BASE_IMAGE_TAG as install-scrapyd

RUN python -m venv /opt/venv --upgrade-deps
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git

RUN curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion -o /tmp/scrapy_bash_completion

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -U \
        git+https://github.com/scrapy/scrapyd.git \
        botocore \
        bs4 \
        cloudscraper \
        logparser

ARG USERNAME
ARG PASSWORD
ARG JOBS_TO_KEEP=5
ARG MAX_PROC=0
ARG MAX_PROC_PER_CPU=4
ARG FINISHED_TO_KEEP=100
ARG POLL_INTERVAL=5.0
ARG BIND_ADDRESS=0.0.0.0
ARG DEBUG=off

COPY ./generate_conf.py /tmp/generate_conf.py
# I should probably run generate_conf.py in an entrypoint script, not at build time
RUN python /tmp/generate_conf.py > /tmp/scrapyd.conf


FROM python:$BASE_IMAGE_TAG AS run-scrapyd

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapyd /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

COPY --from=install-scrapyd /tmp/scrapy_bash_completion /etc/bash_completion.d/scrapy_bash_completion
RUN echo 'source /etc/bash_completion.d/scrapy_bash_completion' >> /root/.bashrc

COPY --from=install-scrapyd /tmp/scrapyd.conf /etc/scrapyd/scrapyd.conf

EXPOSE $HTTP_PORT

#CMD ["scrapyd", "--pidfile="]
#CMD bash -c "mkdir -p /var/lib/scrapyd/logs && scrapyd --pidfile="
CMD bash -c "mkdir -p ${DATA_DIR}/logs && scrapyd --pidfile="
