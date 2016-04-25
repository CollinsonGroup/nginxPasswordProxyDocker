#!/bin/bash
set -e
echo Configuring nginx
python /configScripts/createNginxConfig.py

echo '$PASSTHRU_USERNAME'
echo '$PASSTHRU_PASSWORD'

echo Setting Password
python /configScripts/htpasswd.py -c -b /etc/nginx/htpasswd "$PASSTHRU_USERNAME" "$PASSTHRU_PASSWORD"

exec "$@"
