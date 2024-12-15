from django.urls import path
from design.views import (
    home_page_view, 
    about_page_view, 
    contact_page_view, 
    portfolio_detail_view, 
    portfolio_page_view, 
    resume_page_view, 
    services_page_view, 
    contact_success_view,
    music_portfolio_view
)

urlpatterns = [
    path('', home_page_view, name="home"),
    path('about/', about_page_view, name="about"),
    path('contact/', contact_page_view, name="contact"),
    path('portfolio/', portfolio_page_view, name="portfolio"),
    path('portfolio/<str:project_id>/', portfolio_detail_view, name='portfolio_detail'),
    path('resume/', resume_page_view, name="resume"),
    path('services/', services_page_view, name="services"),
    path('contact/success/', contact_success_view, name='contact_success'),
     path('music-portfolio/', music_portfolio_view, name='music_portfolio'),
]

