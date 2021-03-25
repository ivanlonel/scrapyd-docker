#!/bin/bash
set -Eeuo pipefail

mkdir -p /etc/scrapyd

python /tmp/generate_conf.py > /etc/scrapyd/scrapyd.conf

mkdir -p "${DATA_DIR}/logs"

exec scrapyd
