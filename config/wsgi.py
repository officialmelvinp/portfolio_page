import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Add this for Vercel
def handler(request, **kwargs):
    return application(request, **kwargs)