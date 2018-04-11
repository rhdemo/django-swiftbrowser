#!/usr/bin/env bash


pip install django==1.09
pip install django-swiftbrowser
unalias cp
cp ./swiftbrowser/*.py /usr/lib/python2.7/site-packages/swiftbrowser/.
cp ./swiftbrowser/templates/*.html /usr/lib/python2.7/site-packages/swiftbrowser/templates/.
cp storageui.service /etc/systemd/system/.
chmod 664 /etc/systemd/system/storageui.service
systemctl daemon-reload
systemctl start storageui.service
systemctl enable storageui