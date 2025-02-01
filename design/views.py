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
        'other_skills': ['PostgreSQL', 'SQLite', 'Pandas', 'NumPy', 'Selenium', 'GitHub', 'Data Analysis', 'API Integration', 'Cloud Deployment (Render)', 'Business Optimization', 'Financial Analytics', 'Next.js', 'React', 'Tailwind CSS', 'Supabase', 'Vercel'],
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
                'title': 'Dolapo Udekwe Makeup Artist Website',
                'short_description': 'Full-stack Next.js website for a professional makeup artist',
                'technologies': ['Next.js', 'React', 'Tailwind CSS', 'Supabase', 'Vercel'],
                'github_url': 'https://github.com/officialmelvinp/makeup_website',
                'live_link': 'https://dolapoudekwe.co.uk',
                'details': [
                    'Developed a responsive full-stack website using Next.js and Tailwind CSS',
                    'Implemented an online booking system with real-time availability',
                    'Integrated with Supabase for backend functionality and data management',
                    'Utilized server-side rendering for improved SEO performance',
                    'Deployed and managed the site using Vercel for optimal performance'
                ]
            },
            {
                'title': 'Library API',
                'short_description': 'Comprehensive library management system',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'Django REST Framework'],
                'github_url': 'https://github.com/officialmelvinp/library-api',
                'details': [
                    'Developed a robust API for managing library resources and user interactions',
                    'Implemented advanced filtering and search capabilities',
                    'Integrated with PostgreSQL for efficient data management',
                    'Utilized Django signals for automated status updates and notifications'
                ]
            },
            {
                'title': 'IMF Web Scraping',
                'short_description': 'Data analysis of IMF economic indicators',
                'technologies': ['Python', 'BeautifulSoup', 'Pandas', 'NumPy'],
                'github_url': 'https://github.com/officialmelvinp/group5-da-dev-db',
                'details': [
                    'Automated data extraction from IMF website using BeautifulSoup',
                    'Performed comprehensive analysis of economic indicators using Pandas and NumPy',
                    'Generated visualizations to highlight trends and patterns in global economic data',
                    'Produced actionable insights for economic forecasting and policy analysis'
                ]
            },
            {
                'title': 'Healthcare Appointment',
                'short_description': 'Appointment booking system for healthcare',
                'technologies': ['Python', 'Django', 'PostgreSQL', 'Django REST Framework'],
                'github_url': 'https://github.com/officialmelvinp/healthcare_app',
                'details': [
                    'Built a secure and efficient appointment booking system for healthcare providers',
                    'Implemented real-time scheduling and management features',
                    'Integrated with healthcare provider calendars for seamless coordination',
                    'Developed automated reminders and notifications for patients and staff'
                ]
            },
            {
                'title': 'Financial Analytics for Renergy Hub',
                'short_description': 'Real-time financial analytics system',
                'technologies': ['Python', 'Django', 'Pandas', 'NumPy', 'Financial APIs'],
                'github_url': 'https://github.com/InternPulse/renergy-hub-django-backend',
                'live_link': 'https://www.renergyhub.com.ng',
                'details': [
                    'Developed a real-time financial analytics system for renewable energy projects',
                    'Created custom dashboards for different stakeholders to visualize key metrics',
                    'Implemented predictive analytics for project outcomes and financial forecasting',
                    'Integrated with multiple data sources and financial APIs for comprehensive analysis'
                ]
            },
            {
                'title': 'Product Management',
                'short_description': 'Efficient product management system',
                'technologies': ['Python', 'Django', 'SQLite'],
                'github_url': 'https://github.com/officialmelvinp/product_management',
                'details': [
                    'Designed and implemented a product management system for e-commerce platforms',
                    'Developed features for inventory tracking, order processing, and supplier management',
                    'Implemented automated reordering system based on inventory levels and sales data',
                    'Created analytics and reporting tools for product performance evaluation'
                ]
            }
        ]
    }
    return render(request, 'main/about.html', context)


def contact_page_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            # Prepare email content
            subject = f'Contact Form Message from {name}'
            email_message = f"""
            Name: {name}
            Email: {email}
            Message:
            {message}
            """
            
            # Send email using CONTACT_EMAIL instead of ADMIN_EMAIL
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],  # Use CONTACT_EMAIL here
                fail_silently=False,
            )

            return JsonResponse({'status': 'success', 'message': 'Email sent successfully!'})

        except Exception as e:
            import traceback
            print(f"Error sending email: {str(e)}")
            print(f"Traceback: {traceback.format_exc()}")
            return JsonResponse({
                'status': 'error',
                'message': str(e) if settings.DEBUG else 'Failed to send message. Please try again.'
            }, status=500)

    return render(request, 'main/contact.html')

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
            'github_url': 'https://github.com/InternPulse/renergy-hub-django-backend',
            'live_link': 'https://www.renergyhub.com.ng'
        },
        {
            'id': 'product-management',
            'title': 'Product Management',
            'short_description': 'Efficient product management system',
            'image': 'img/product.jpg',
            'category': 'Management',
            'github_url': 'https://github.com/officialmelvinp/product_management'
        },
        {
            'id': 'dolapo-udekwe-makeup',
            'title': 'Dolapo Udekwe Makeup Artist Website',
            'short_description': 'Full-stack Next.js website for a professional makeup artist',
            'image': 'img/dolapo.jpeg',
            'category': 'Full-Stack Development',
            'github_url': 'https://github.com/officialmelvinp/makeup_website',
            'live_link': 'https://dolapoudekwe.co.uk',
        },
    ]
    services = [
        {
            'icon': 'bi bi-code-slash',
            'title': 'Backend Development',
            'description': 'Scalable and efficient server-side solutions.',
            'tags': ['Python', 'Django', 'API Development']
        },
        {
            'icon': 'bi bi-graph-up',
            'title': 'Data Analysis',
            'description': 'Insightful data processing and visualization.',
            'tags': ['Python', 'Pandas', 'Data Visualization']
        },
        {
            'icon': 'bi bi-gear',
            'title': 'Business Process Optimization',
            'description': 'Streamlining operations for maximum efficiency.',
            'tags': ['Process Mapping', 'Automation', 'KPI Tracking']
        }
    ]
    
    recommendation = {
            'name': 'Djinee john',
            'text': "I highly recommend Ajayi Adeboye, who was a backend engineer intern during our 5th cohort at InternPulse. During his time with us, he displayed remarkable technical skills and a strong work ethic. Adeboye contributed significantly to Renergy Hub, a cleantech platform, showing his ability to apply his backend engineering expertise in real-world scenarios. He was always proactive in solving complex problems, and his collaboration with the team was seamless. Adeboye consistently went above and beyond, and his leadership in his role was evident as he contributed to the platform's development and performance.",
            'author': 'Founder and Chief Mentor',
            'position': 'InternPulse',
    }
    
    context = {
        'projects': projects,
        'services': services,
        'recommendation': recommendation
        
    }
    return render(request, "main/portfolio.html", context)

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
        
         'dolapo-udekwe-makeup': {
            'title': 'Dolapo Udekwe Makeup Artist Website',
            'description': 'A full-stack Next.js website for a professional makeup artist, featuring a responsive design, online booking system, and portfolio showcase.',
            'category': 'Full-Stack Development',
            'project_type': 'Web Development',
            'project_date': 'March 2025',
            'github_url': 'https://github.com/officialmelvinp/makeup_website',
            'live_link': 'https://dolapoudekwe.co.uk',
            'details': [
                'Responsive design using Tailwind CSS',
                'Server-side rendering with Next.js for improved SEO',
                'Integration with Supabase for backend functionality',
                'Online booking system with real-time availability',
                'Dynamic portfolio showcase with image optimization',
                'Admin dashboard for content management'
            ],
            'images': [
                'img/dolapo.jpeg',
            ],
            'technologies': ['Next.js', 'React', 'Tailwind CSS', 'Supabase', 'Vercel']
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
            'live_link': 'https://www.renergyhub.com.ng',
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
        },
        
    ]

    context = {
        'services': services,
        'testimonials': testimonials
    }

    return render(request, 'main/services.html', context)

