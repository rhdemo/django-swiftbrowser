from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from swiftbrowser.views import containerview,containerview2, objectview, download,\
    delete_object, login, tempurl, upload, create_pseudofolder,\
    create_container, delete_container, public_objectview, toggle_public,\
    edit_acl, clouds, cloudview

urlpatterns = patterns(
    'swiftbrowser.views',
    url(r'^login/$', login, name="login"),
    url(r'^clouds/$', clouds, name="clouds"),
    url(r'^alt/$', containerview2, name="containerview2"),
    url(r'^$', containerview, name="containerview"),
    url(r'^public/(?P<account>.+?)/(?P<container>.+?)/(?P<prefix>(.+)+)?$',
        public_objectview, name="public_objectview"),
    url(r'^toggle_public/(?P<container>.+?)/$', toggle_public,
        name="toggle_public"),
    url(r'^tempurl/(?P<container>.+?)/(?P<objectname>.+?)$', tempurl,
        name="tempurl"),
    url(r'^upload/(?P<container>.+?)/(?P<prefix>.+)?$', upload, name="upload"),
    url(r'^create_pseudofolder/(?P<container>.+?)/(?P<prefix>.+)?$',
        create_pseudofolder, name="create_pseudofolder"),
    url(r'^create_container$', create_container, name="create_container"),
    url(r'^delete_container/(?P<container>.+?)$', delete_container,
        name="delete_container"),
    url(r'^download/(?P<container>.+?)/(?P<objectname>.+?)$', download,
        name="download"),
    url(r'^delete/(?P<container>.+?)/(?P<objectname>.+?)$', delete_object,
        name="delete_object"),
    url(r'^objects/(?P<container>.+?)/(?P<prefix>(.+)+)?$', objectview,
        name="objectview"),
    url(r'^cloudview/(?P<cloud>.+?)/(?P<prefix>(.+)+)?$', cloudview,
        name="cloudview"),
    url(r'^acls/(?P<container>.+?)/$', edit_acl, name="edit_acl"),
)
urlpatterns += patterns('django.views.static',(r'^static/(?P<path>.*)','serve',{'document_root':settings.STATIC_ROOT}), )