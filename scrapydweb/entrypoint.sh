#!/bin/bash
set -Eeuo pipefail

SETTINGS_FILE = $(pip show logparser | sed -n 's/^Location: //gp')/logparser/settings.py
sed -i "s/^OVERRIDE_TELNET_CONSOLE_HOST = ''/OVERRIDE_TELNET_CONSOLE_HOST = '${TELNET_CONSOLE_HOST}'/g" $SETTINGS_FILE

exec scrapydweb