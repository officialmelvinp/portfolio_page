from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_page.settings')
application = get_wsgi_application()

def handler(request, **kwargs):
    return application(request, **kwargs)