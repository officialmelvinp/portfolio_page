import os
from django.core.wsgi import get_wsgi_application
from django.core.exceptions import ImproperlyConfigured

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    application = get_wsgi_application()
except ImproperlyConfigured as e:
    print(f"Error in WSGI application: {str(e)}")
    raise

def handler(event, context):
    try:
        return application(event, context)
    except Exception as e:
        print(f"Error in handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }

