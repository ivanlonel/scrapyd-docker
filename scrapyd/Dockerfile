ARG PYTHON_VERSION=3-slim


FROM python:$PYTHON_VERSION as install-scrapyd

RUN apt-get update && apt-get install -y --no-install-recommends gcc git curl build-essential

RUN curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion -o /tmp/scrapy_bash_completion

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN python -m pip install --upgrade pip && pip install -U git+https://github.com/scrapy/scrapyd.git

COPY ./generate_conf.py /tmp/generate_conf.py
RUN python /tmp/generate_conf.py > /tmp/scrapyd.conf


FROM python:$PYTHON_VERSION AS run-scrapyd

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapyd /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

COPY --from=install-scrapyd /tmp/scrapy_bash_completion /etc/bash_completion.d/scrapy_bash_completion
RUN echo 'source /etc/bash_completion.d/scrapy_bash_completion' >> /root/.bashrc

COPY --from=install-scrapyd /tmp/scrapyd.conf /etc/scrapyd/scrapyd.conf

ARG HTTP_PORT=6800
EXPOSE $HTTP_PORT

CMD ["scrapyd", "--pidfile="]
