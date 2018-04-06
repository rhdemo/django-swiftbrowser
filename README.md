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
   
   git clone https://github.com/rhdemo/django-swiftbrowser.git
   
   cd django-swiftbrowser
   
   ** UPDATE SETTINGS NOW **
   
   Update the ./swiftbrowser/settings.py file
   
   pip install django-swiftbrowser
   
2) Update the custom files including the setting ot where swiftbrowser is installed on the system
    
    From git clone dir:
    
    cp ./swiftbrowser/*.py  /usr/lib/python2.7/site-packages/swiftbrowser/.
    
    cp ./swiftbrowser/templates/*.html /usr/lib/python2.7/site-packages/swiftbrowser/templates/. 


3) Please make sure that "tempurl" (optional without auth) and "formpost" middlewares are activated in your proxy server. Extract from /etc/swift/proxy-server.conf:

    [pipeline:main]
    pipeline = catch_errors gatekeeper healthcheck proxy-logging cache tempurl formpost tempauth proxy-logging proxy-server

    [filter:tempurl]
    use = egg:swift#tempurl

    [filter:formpost]
    use = egg:swift#formpost
    
4) For simple testing, run development server:

    django-admin runserver 0.0.0.0:80 --settings=swiftbrowser.settings

5) For more performance, setup a service:

    `touch /etc/systemd/system/storageui.service`
    
    `chmod 664 /etc/systemd/system/storageui.service`
    
    `vi /etc/systemd/system/storageui.service`
    

    ```
    [Unit]
    Description=Storage UI based off the swiftbrowser for RHSUmmit2018
    After=network.target
    
    [Service]
    ExecStart=/usr/bin/django-admin runserver 0.0.0.0:80 --settings=swiftbrowser.settings
    Type=simple
    PIDFile=~/.
    Restart=always
    
    [Install]
    WantedBy=default.target```


   `systemctl daemon-reload`
  
   `systemctl start storageui.service`
  
   `systemctl enable storageui`


6) Open "http://<hostname>/" in your browser and use 'demo' (pw: demo)to login when there is no auth or 'account:username' to login with tempauth .


Screenshots
-----------

![Login screen](screenshots/00.png)
![Container view](screenshots/01.png)
![Object view](screenshots/02.png)
