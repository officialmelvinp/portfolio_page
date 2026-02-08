from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from design.views import key_projects 

class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'portfolio', 'music_portfolio', 'contact']

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        # This assumes key_projects is a list of dictionaries with an 'id' key
        # In a real Django app, this would typically query a database model
        return [p['id'] for p in key_projects]

    def location(self, item):
        return reverse('portfolio_detail', args=[item])

    def lastmod(self, item):
        # If your projects had a 'last_updated' field, you would return it here.
        # For now, returning None or a fixed date is acceptable if not dynamic.
        return None # Or a datetime object if available, e.g., datetime.date(2024, 7, 25)
