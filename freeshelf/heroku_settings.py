from freeshelf.settings import *
import django_heroku

DEBUG = False

# Activate Django-Heroku.
django_heroku.settings(locals())
