ARG BASE_IMAGE_TAG=3.9-slim


FROM python:$BASE_IMAGE_TAG as install-scrapydweb

RUN apt-get update && \
    apt-get install -y --no-install-recommends git

ENV PATH="/opt/venv/bin:$PATH"
RUN python -m venv /opt/venv --upgrade-deps && \
    pip install --no-cache-dir -U git+https://github.com/my8100/scrapydweb.git


FROM python:$BASE_IMAGE_TAG AS run-scrapydweb

ARG VENV_PATH=/opt/venv
COPY --from=install-scrapydweb /opt/venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

ARG TELNET_CONSOLE_HOST
# This should probably be done in an entrypoint script with an env var instead of a build arg
RUN sed -i "s/^OVERRIDE_TELNET_CONSOLE_HOST = ''/OVERRIDE_TELNET_CONSOLE_HOST = '${TELNET_CONSOLE_HOST}'/g" \
    $(pip show logparser | sed -n 's/^Location: //gp')/logparser/settings.py

WORKDIR /app
COPY ./scrapydweb_settings_v*.py .

ARG HTTP_PORT=5000
EXPOSE $HTTP_PORT

CMD ["scrapydweb"]
