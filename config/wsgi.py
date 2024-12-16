import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

def handler(event, context):
    return application(event.get('headers', {}), event.get('body', ''))