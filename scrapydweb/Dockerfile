ARG PYTHON_VERSION=3.9-slim


FROM python:$PYTHON_VERSION as install-scrapydweb

RUN python -m venv /opt/venv --upgrade-deps
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends git && \
    python -m pip install --upgrade pip && \
	pip install -U git+https://github.com/my8100/scrapydweb.git


FROM python:$PYTHON_VERSION AS run-scrapydweb

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapydweb /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

RUN DIR=$(pip show logparser | sed -n 's/^Location: //gp') && \
    sed -i "s/^OVERRIDE_TELNET_CONSOLE_HOST = ''/OVERRIDE_TELNET_CONSOLE_HOST = '${TELNET_CONSOLE_HOST}'/g" ${DIR}/logparser/settings.py && \
    grep ${DIR}/logparser/settings.py -e "OVERRIDE_TELNET_CONSOLE_HOST"

WORKDIR /app
COPY ./scrapydweb_settings_v*.py .

#RUN ln -ns $(pip show logparser | sed -n 's/^Location: //gp')/logparser ./logparser
#COPY ./logparser_settings.py ./logparser/settings.py

EXPOSE 5000

CMD ["scrapydweb"]
