from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission
import requests
import random
from django.http import JsonResponse
import json



def home_page_view(request):
    # Generate random positions for animated elements
    num_elements = 6
    positions = [
        {
            'left': random.randint(0, 100),
            'top': random.randint(0, 100),
            'delay': random.randint(0, 5)
        }
        for _ in range(num_elements)
    ]

    context = {
        'positions': positions,
    }

    return render(request, 'main/index.html', context)



def about_page_view(request):
    context = {
        'other_skills': ['PostgreSQL', 'SQLite', 'Pandas', 'NumPy', 'Selenium', 'GitHub', 'Data Analysis', 'API Integration', 'Cloud Deployment (Render)', 'Business Optimization', 'Financial Analytics'],
        'work_experience': [
            {
                'title': 'Backend Development Intern',
                'company': 'InternPulse (Remote)',
                'duration': 'October 2024 – Present',
                'responsibilities': [
                    'Designed and implemented scalable backend APIs for Library Management, Healthcare Appointment, and Product Management systems.',
                    'Collaborated with cross-functional teams to refine API functionality, ensuring robust filtering, search capabilities, and error handling.',
                    'Automated data scraping using Selenium to support the analytics team.',
                    'Built financial analytics APIs, integrating databases with external APIs to generate real-time insights.'
                ]
            },
            {
                'title': 'Operations Support',
                'company': 'Premier Lottery, Lagos',
                'duration': '2017 – Present',
                'responsibilities': [
                    'Managed operations across 50+ outlets, improving efficiency by 15% through supervision, data-driven decision-making, and performance monitoring.',
                    'Adapted to economic shifts by optimizing budgets and achieving a 20% increase in sales over three years.',
                    'Conducted audits and ensured regulatory compliance, safeguarding the company from financial risks.'
                ]
            }
        ],
        'education': {
            'degree': 'Bachelor of Science in Accounting',
            'university': 'Olabisi Onabanjo University'
        },
        'certifications': [
            'Backend with Python Django (Univelcity)',
            'Data Analytics Professional Program (One Campus Academy)'
        ],
        'projects': [
            {
                'title': 'Library API',
                'short_description': 'Comprehensive library management system',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'Django REST Framework'],
            },
            {
                'title': 'IMF Web Scraping',
                'short_description': 'Data analysis of IMF economic indicators',
                'technologies': ['Python', 'BeautifulSoup', 'Pandas', 'NumPy'],
            },
            {
                'title': 'Healthcare Appointment',
                'short_description': 'Appointment booking system for healthcare',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'Django REST Framework'],
            },
            {
                'title': 'Financial Analytics for Renergy Hub',
                'short_description': 'Real-time financial analytics system',
                'technologies': ['Python', 'Django', 'Pandas', 'NumPy', 'Financial APIs'],
            },
            {
                'title': 'Product Management',
                'short_description': 'Efficient product management system',
                'technologies': ['Python', 'Django', 'SQLite'],
            }
        ]
    }
    return render(request, 'main/about.html', context)






def contact_page_view(request):
    if request.method == 'GET':
        return render(request, "main/contact.html")
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Save to database
        ContactSubmission.objects.create(name=name, email=email, message=message)

        # Send email
        try:
            send_mail(
                subject=f"New contact form submission from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            email_sent = True
        except Exception as e:
            email_sent = False
            print(f"Error sending email: {str(e)}")

        return JsonResponse({
            "status": "success" if email_sent else "error",
            "message": "Form submitted successfully" if email_sent else "Error sending email"
        })

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def contact_success_view(request):
    return render(request, "main/contact_success.html")




def portfolio_page_view(request):
    projects = [
        {
            'id': 'library-api',
            'title': 'Library API',
            'short_description': 'Comprehensive library management system',
            'image': 'img/library.jpg',
            'category': 'API',
            'github_url': 'https://github.com/officialmelvinp/library-api'
        },
        {
            'id': 'imf-analysis',
            'title': 'IMF Web Scraping',
            'short_description': 'Data analysis of IMF economic indicators',
            'image': 'img/imf.jpg',
            'category': 'Data Analysis',
            'github_url': 'https://github.com/officialmelvinp/group5-da-dev-db'
        },
        {
            'id': 'healthcare-app',
            'title': 'Healthcare Appointment',
            'short_description': 'Appointment booking system for healthcare',
            'image': 'img/health.jpg',
            'category': 'API',
            'github_url': 'https://github.com/officialmelvinp/healthcare_app'
        },
        {
            'id': 'renergy-hub',
            'title': 'Financial Analytics for Renergy Hub',
            'short_description': 'Real-time financial analytics system',
            'image': 'img/renergy.jpg',
            'category': 'Data Analysis',
            'github_url': 'https://github.com/InternPulse/renergy-hub-django-backend'
        },
        {
            'id': 'product-management',
            'title': 'Product Management',
            'short_description': 'Efficient product management system',
            'image': 'img/product.jpg',
            'category': 'Management',
            'github_url': 'https://github.com/officialmelvinp/product_management'
        }
    ]
    return render(request, "main/portfolio.html", {'projects': projects})

def portfolio_detail_view(request, project_id):
    projects = {
        'library-api': {
            'title': 'Library API',
            'description': 'A comprehensive library management system with advanced features and robust API',
            'category': 'Backend Development',
            'project_type': 'API Development',
            'project_date': 'October 2024',
            'github_url': 'https://github.com/officialmelvinp/library-api',
            'details': [
                'Advanced filtering capabilities by title, author, and genre',
                'Integration with PostgreSQL for efficient data management',
                'Implementation of Django signals for automated status updates',
                'Deployment on Render for real-time data handling and scalability'
            ],
            'images': [
                'img/library.jpg',
               
            ]
        },
        'imf-analysis': {
            'title': 'IMF Web Scraping',
            'description': 'Data analysis of IMF economic indicators',
            'category': 'Data Analysis',
            'project_type': 'Web Scraping & Analysis',
            'project_date': 'September 2024',
            'github_url': 'https://github.com/officialmelvinp/group5-da-dev-db',
            'details': [
                'Automated data extraction from IMF website',
                'Comprehensive analysis of economic indicators',
                'Visualization of trends and patterns',
                'Insights generation for economic forecasting'
            ],
            'images': [
                'img/imf.jpg',
                
            ]
        },
        'healthcare-app': {
            'title': 'Healthcare Appointment',
            'description': 'Appointment booking system for healthcare providers',
            'category': 'Backend Development',
            'project_type': 'API Development',
            'project_date': 'November 2024',
            'github_url': 'https://github.com/officialmelvinp/healthcare_app',
            'details': [
                'Secure patient data management',
                'Real-time appointment scheduling and management',
                'Integration with healthcare provider calendars',
                'Automated reminders and notifications'
            ],
            'images': [
                'img/health.jpg',
                
            ]
        },
        'renergy-hub': {
            'title': 'Financial Analytics for Renergy Hub',
            'description': 'Real-time financial analytics system for renewable energy projects',
            'category': 'Data Analysis',
            'project_type': 'Financial Analytics',
            'project_date': 'December 2024',
            'github_url': 'https://github.com/InternPulse/renergy-hub-django-backend',
            'details': [
                'Real-time data processing of financial metrics',
                'Custom dashboards for different stakeholders',
                'Predictive analytics for project outcomes',
                'Integration with multiple data sources and APIs'
            ],
            'images': [
                'img/renergy.jpg',
                
            ]
        },
        'product-management': {
            'title': 'Product Management',
            'description': 'Efficient product management system for e-commerce platforms',
            'category': 'Management',
            'project_type': 'Backend Development',
            'project_date': 'January 2025',
            'github_url': 'https://github.com/officialmelvinp/product_management',
            'details': [
                'Inventory tracking and management',
                'Order processing and fulfillment',
                'Supplier management and reordering automation',
                'Analytics and reporting for product performance'
            ],
            'images': [
                'img/product.jpg',
                
            ]
        }
    }
    project = projects.get(project_id)
    if project is None:
        raise Http404("Project does not exist")
    return render(request, "main/portfolio-details.html", {'project': project})





    # Add songs with titles, links, and image URLs
def music_portfolio_view(request):
    # Bio information
    name = getattr(settings, 'ARTIST_NAME', 'Melvin-P')
    bio = getattr(
        settings,
        'ARTIST_BIO',
        (
            "Meet Ajayi Adeboye Samuel, widely celebrated as Melvin-P, a visionary songwriter and dynamic performer "
            "whose musical journey began in the vibrant landscapes of Ogun State and flourished in the pulsating heart "
            "of Lagos, Nigeria. Born into a family where music wasn't just listened to but lived, Melvin-P's artistic DNA "
            "was shaped by the rich sounds of African music legends and contemporary giants like 2face and Plantashun Boyz.\n\n"
            "From penning his first lyrics at 15, Melvin-P has evolved into a formidable force in the Nigerian music scene. "
            "His natural talent for songwriting, combined with his distinctive voice and magnetic stage presence, has earned "
            "him recognition across multiple platforms. His breakthrough moment came with an impressive second runner-up "
            "finish in the Top Radio Next Top Rated Competition (Season 3), setting the stage for even greater achievements.\n\n"
            "Recent Achievements:\n"
            "▸ Winner of the prestigious VYBR Session 4 Competition (2023), claiming the title of Best Act with his breakthrough track 'Wonder'\n"
            "▸ Secured a remarkable victory with the highest number of votes and a grand prize of ₦2 million\n"
            "▸ Released chart-topping singles including 'Everyday' and 'Wonder' (2023-2024)\n\n"
            "Known for his versatility and innovative approach to music, Melvin-P has made waves with his impressive catalog of cover tracks, "
            "paying homage to A-List artists while adding his unique flavor. His original compositions, particularly 'Wonder' and 'Everyday,' "
            "showcase his evolution as an artist and his ability to create music that resonates with diverse audiences.\n\n"
            "Now in 2024, Melvin-P, also known as 'The Deity,' continues to push boundaries and redefine contemporary Nigerian music. "
            "With each release, he demonstrates why he's not just another artist, but a force destined to leave an indelible mark on the "
            "African music landscape."
        ),
    )
    profile_image = getattr(settings, 'ARTIST_PROFILE_IMAGE', 'img/winner.jpeg')
    # Existing songs list
    songs = [
        {
            'title': 'Stream Melvin P Wonder on Youtube',
            'youtube': 'https://youtu.be/k0bdt_Hv_1c?si=NWvsUQuZ4XDDHg5C',
            'image': 'img/clout.jpeg'
        },
        {
            'title': 'Everyday',
            'link': 'https://linktr.ee/melvin_p',
            'image': 'img/everyday.jpeg'
        },
        {
            'title': 'Wonder',
            'link': 'https://linktr.ee/melvin_p',
            'image': 'img/wonder.jpeg' 
        },
        {
            'title': 'Thanking God',
            'link': 'https://linktr.ee/melvin_p',
            'image': 'img/thanking_god.jpeg'
        },
        {
            'title': 'Happy Day',
            'link': 'https://linktr.ee/melvin_p',
            'image': 'img/happy_day.jpeg'
        },
    ]

    context = {
        'name': name,
        'bio': bio,
        'profile_image': profile_image,
        'songs': songs,
    }

    return render(request, 'main/music_portfolio.html', context)

def resume_page_view(request):
    return render(request, "main/resume.html")

def services_page_view(request):
    services = [
        {
            'title': 'Backend Development',
            'icon': 'fas fa-code',
            'description': 'Robust and scalable backend solutions tailored to your business needs.',
            'features': [
                'Custom API development',
                'Database design and optimization',
                'Authentication and security implementation',
            ],
            'technologies': ['Python', 'Django', 'PostgreSQL', 'RESTful APIs']
        },
        {
            'title': 'Data Engineering & Analytics',
            'icon': 'fas fa-chart-line',
            'description': 'Transform raw data into actionable insights for informed decision-making.',
            'features': [
                'Data pipeline development',
                'ETL process implementation',
                'Advanced analytics and visualizations',
            ],
            'technologies': ['Pandas', 'NumPy', 'Selenium']
        },
        {
            'title': 'Financial Analysis',
            'icon': 'fas fa-calculator',
            'description': 'Comprehensive financial solutions to drive your business forward.',
            'features': [
                'Financial modeling and forecasting',
                'Business intelligence dashboards',
                'Risk assessment and management',
            ],
            'technologies': ['Excel', 'Python', 'SQL']
        },
        {
            'title': 'Process Optimization',
            'icon': 'fas fa-cogs',
            'description': 'Streamline operations and boost efficiency through technology integration.',
            'features': [
                'Business process analysis',
                'Workflow automation',
                'Performance metrics and KPI tracking',
            ],
            'technologies': ['Lean Six Sigma', 'Automation tools', 'Process mapping software']
        },
        {
            'title': 'System Architecture',
            'icon': 'fas fa-network-wired',
            'description': 'Design scalable and efficient system architectures for optimal performance.',
            'features': [
                'Microservices architecture design',
                'Cloud-based solutions implementation',
                'Scalability and performance optimization',
            ],
            'technologies': ['AWS', 'Docker', 'Kubernetes', 'Microservices']
        },
    #     {
    #         'title': 'Innovation Consulting',
    #         'icon': 'fas fa-lightbulb',
    #         'description': 'Strategic guidance on technology adoption and digital transformation.',
    #         'features': [
    #             'Technology stack assessment and recommendations',
    #             'Digital transformation roadmap development',
    #             'Emerging technology integration strategies',
    #         ],
    #         'technologies': ['AI/ML', 'Blockchain', 'IoT', 'Cloud Computing']
    #     },
     ]

    testimonials = [
        
        {
            'content': "Ajayi's expertise in backend development and data analytics has been instrumental in scaling our operations. His insights have directly contributed to a 30% increase in our operational efficiency.",
            'author': 'Pere Afezu'
        },
        {
            'content': 'The financial analysis tools developed by Ajayi have revolutionized our decision-making process. We now have real-time insights that have improved our profitability by 25%.',
            'author': 'ifeka odira hilary'
        }
    ]

    context = {
        'services': services,
        'testimonials': testimonials
    }

    return render(request, 'main/services.html', context)

