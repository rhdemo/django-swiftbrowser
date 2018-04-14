""" Settings for Django project """
import os

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

USE_L10N = True
USE_TZ = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

ROOT_URLCONF = 'swiftbrowser.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'swiftbrowser',
)


#Update values below to correct URL
SWIFT_CLOUD='Azure'
#SWIFT_CLOUD='AWS'
#SWIFT_CLOUD='Google Cloud'
#SWIFT_CLOUD='Local'

#Buckets for each cloud
AWS_BUCKETS='bucket1,bucket2,bucket3'
AZURE_BUCKETS='bucket7,bucket8,bucket9'
GCE_BUCKETS='bucket4,bucket5,bucket6'
PRIVATE_BUCKETS='bucket10,bucket11,bucket12'
TEST_BUCKETS='test1,test2,test3'

SWIFT_VOLUME='gv0'
SWIFT_HOST='localhost'
SWIFT_PORT='8080'
SWIFT_AUTH_URL = 'http://' + SWIFT_HOST + ':' + SWIFT_PORT + '/auth/v1.0'
SWIFT_AUTH_VERSION = 1  # 2 for keystone
STORAGE_URL = 'http://' + SWIFT_HOST + ':' + SWIFT_PORT + '/v1/AUTH_' + SWIFT_VOLUME
BASE_URL = 'http://' + SWIFT_HOST  # default if using built-in runserver

TIME_ZONE = 'America/Boise'
LANGUAGE_CODE = 'en-en'
SECRET_KEY = 'DONT_USE_THIS_IN_PRODUCTION'
#STATIC_URL = "http://cdnjs.cloudflare.com/ajax/libs/"

ALLOWED_HOSTS = ['127.0.0.1', '*']

STATICFILES_DIRS = (os.path.join( os.path.dirname( __file__ ), 'static' ),)
STATICILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',)
STATIC_URL = '/static/'
STATIC_ROOT = '/usr/lib/python2.7/site-packages/swiftbrowser/static/'

