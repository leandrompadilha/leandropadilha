import environ

from mysite.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default':env.db(),
}