#!/bin/bash

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
celery -A leaf.celery.celery beat -l info
