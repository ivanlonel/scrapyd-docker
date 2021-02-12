ARG PYTHON_VERSION=3-slim


FROM python:$PYTHON_VERSION as install-scrapydweb

RUN apt-get update && apt-get install -y --no-install-recommends git

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN python -m pip install --upgrade pip && pip install -U git+https://github.com/my8100/scrapydweb.git


FROM python:$PYTHON_VERSION AS run-scrapydweb

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapydweb /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# RUN ln -ns $(pip show scrapydweb | sed -n 's/^Location: //gp')/scrapydweb /var/lib/scrapydweb

COPY ./scrapydweb_settings_v*.py /app/
WORKDIR /app

EXPOSE 5000

CMD scrapydweb
