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
   
   pip install django==1.09
   
   git clone 
   
   cd django-swiftbrowser
   
   ** UPDATE SETTINGS NOW **
   
   Update the ./swiftbrowser/settings.py file
   
   python setup.py install
   
   
   (alt: pip install django-swiftbrowser plus other steps with copy files)


2) Please make sure that "tempurl" and "formpost" middlewares are activated in your proxy server. Extract from /etc/swift/proxy-server.conf:

    [pipeline:main]
    pipeline = catch_errors gatekeeper healthcheck proxy-logging cache tempurl formpost tempauth proxy-logging proxy-server

    [filter:tempurl]
    use = egg:swift#tempurl

    [filter:formpost]
    use = egg:swift#formpost
3) ONLY IF YOU DID ALT INSTALL: Update the settings.py file for your settings. It is located somewhere like: /usr/lib/python2.7/site-packages/swiftbrowser/settings.py
    
    From git clone dir:
    
    cp ./swiftbrowser/views.py ./swiftbrowser/settings.py /usr/lib/python2.7/site-packages/swiftbrowser/.
    
    cp ./swiftbrowser/templates/containerview.html ./swiftbrowser/templates/objectview.html /usr/lib/python2.7/site-packages/swiftbrowser/templates/. 
4) Run development server:

    django-admin runserver 0.0.0.0:80 --settings=swiftbrowser.settings

5) Open "http://<hostname>/" in your browser and use 'demo' (pw: demo)to login when there is no auth or 'account:username' to login with tempauth .


Screenshots
-----------

![Login screen](screenshots/00.png)
![Container view](screenshots/01.png)
![Object view](screenshots/02.png)
