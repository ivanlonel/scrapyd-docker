#!/bin/bash
set -Eeuo pipefail

SETTINGS_FILE="$(pip show logparser | sed -n 's/^Location: //gp')/logparser/settings.py"
sed -i "s#^SCRAPYD_LOGS_DIR = ''#SCRAPYD_LOGS_DIR = '${LOCAL_SCRAPYD_LOGS_DIR}'#g" "$SETTINGS_FILE"
sed -i "s#^SCRAPYD_SERVER = '127.0.0.1:6800'#SCRAPYD_SERVER = '${LOCAL_SCRAPYD_SERVER}'#g" "$SETTINGS_FILE"
sed -i "s#^OVERRIDE_TELNET_CONSOLE_HOST = ''#OVERRIDE_TELNET_CONSOLE_HOST = '${TELNET_CONSOLE_HOST}'#g" "$SETTINGS_FILE"

exec scrapydweb
