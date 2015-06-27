#!/bin/bash

set -e
set -o nounset
set -o pipefail

RELATIVE_PATH=$(dirname "${BASH_SOURCE[0]}")
FULLPATH=$(cd "$RELATIVE_PATH" && pwd)

docker run -tip 8000:8000 \
    -v $FULLPATH/../:/opt/rahul/ten_thousand_hours \
    -v /var/log/tth:/var/log/tth \
    tth-dev \
    python manage.py runserver 0.0.0.0:8000
