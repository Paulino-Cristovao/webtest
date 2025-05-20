import os
from django.core.wsgi import get_wsgi_application

# tell Django which settings module to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'embassy.settings')

# get the WSGI application callable for your server (e.g. runserver, gunicorn, etc.)
application = get_wsgi_application()
