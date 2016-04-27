#!/bin/bash
set -e
echo Configuring nginx
python /configScripts/createNginxConfig.py

echo Setting Password
python /configScripts/htpasswd.py /etc/nginx/htpasswd

exec "$@"
