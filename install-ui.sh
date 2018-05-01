#!/usr/bin/env bash

if [ -e host.config ]
then

    source host.config
    pip install pip==9.0.3
    pip install django==1.09
    pip install django-swiftbrowser
    alias cp=cp
#    unalias cp
    cp ./swiftbrowser/*.py /usr/lib/python2.7/site-packages/swiftbrowser/.
    cp ./swiftbrowser/templates/*.html /usr/lib/python2.7/site-packages/swiftbrowser/templates/.
    cp -r ./swiftbrowser/static/ /usr/lib/python2.7/site-packages/swiftbrowser/.
    sed -i '50s/.*/SWIFT_HOST="'$SWIFT_HOST'"/' /usr/lib/python2.7/site-packages/swiftbrowser/settings.py
    sed -i '49s/.*/SWIFT_VOLUME="'$SWIFT_VOLUME'"/' /usr/lib/python2.7/site-packages/swiftbrowser/settings.py
    cp storageui.service /etc/systemd/system/.
    chmod 664 /etc/systemd/system/storageui.service
    systemctl daemon-reload
    systemctl start storageui.service
    systemctl enable storageui
    export UI=/usr/lib/python2.7/site-packages/swiftbrowser/

else
    echo "Host config file does not exist.  Please: cp host.config.example host.config; vi host.config and set the host name."
fi