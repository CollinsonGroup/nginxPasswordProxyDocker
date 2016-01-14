#!/bin/bash
set -e
echo Configuring nginx
python /configScripts/createNginxConfig.py

echo Setting Password
python /configScripts/htpasswd.py -c -b /etc/nginx/htpasswd $PASSTHRU_USERNAME $PASSTHRU_PASSWORD

echo $@
#nginx -g 'daemon off;'
exec "$@"
