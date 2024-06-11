# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY='django-insecure-pnayo2qh^mzdn$8ly1&b+ncq@uji354l@qlj(iixydh4^xe6j#'

ALLOWED_HOSTS = ['informed-coaching']

DATABASES = {
    'mysql': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'MYSQL_DATABASE',
        'USER' : 'MYSQL_USER',
        'PASSWORD' : 'MYSQL_PASSWORD',
        'HOST' : 'DB_HOST',
        'PORT' : '3306'
    }
}