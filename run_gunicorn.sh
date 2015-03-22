#!/bin/bash
export ENV=production

LOGDIR=/var/log/tth
LOGFILE=app.log
NUM_WORKERS=2

python manage.py collectstatic --noinput

mkdir ${LOGDIR}

gunicorn ten_thousand_hours.wsgi \
    -w $NUM_WORKERS \
    --timeout 120 \
    --log-level=- \
    --log-file=${LOGDIR}/${LOGFILE} \
    --bind 0.0.0.0:8000
