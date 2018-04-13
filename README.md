django-swiftbrowser for RHDEMO
===================

[![Build Status](https://travis-ci.org/cschwede/django-swiftbrowser.png?branch=master)](https://travis-ci.org/cschwede/django-swiftbrowser)

Simple web app build with Django and Twitter Bootstrap to access Openstack Swift.
* If you want to run the real swiftbrowser, please see the real product page
* No database needed
* Works with no auth and tempauth
* Support for public containers. ACL support in the works
* Minimal interface, usable on your desktop as well as on your smartphone
* Screenshots anyone? See below!

Quick Install
-------------
0) This assumes swift proxy with object server is already install on the server and things like pip are setup

1) Install swiftbrowser:
   
   git clone https://github.com/rhdemo/django-swiftbrowser.git
   
   cd django-swiftbrowser
   
   ./install.sh
   

2) Please make sure that "tempurl" (optional without auth) and "formpost" middlewares are activated in your proxy server. Extract from /etc/swift/proxy-server.conf:

    [pipeline:main]
    pipeline = catch_errors gatekeeper healthcheck proxy-logging cache tempurl formpost tempauth proxy-logging proxy-server

    [filter:tempurl]
    use = egg:swift#tempurl

    [filter:formpost]
    use = egg:swift#formpost
    
3) StorageUI should start automatically

    systemctl status storageui
    
    For simple testing, run development server after stopping service:
    
    systemctl stop storageui
        
    django-admin runserver 0.0.0.0:80 --settings=swiftbrowser.settings

4) Open "http://<hostname>/" in your browser and use 'demo' (pw: demo)to login when there is no auth or 'account:username' to login with tempauth .


Screenshots
-----------

![Login screen](screenshots/00.png)
![Container view](screenshots/01.png)
![Object view](screenshots/02.png)
