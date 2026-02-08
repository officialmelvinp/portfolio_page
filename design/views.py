from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactSubmission 
import random
from django.http import JsonResponse
import json




personal_info = {
    'name': 'Ajayi Adeboye Samuel',
    'title': 'Full-Stack Developer • Backend Engineer • AI & NLP Engineer (In Progress)',
    'tagline': 'Python/Django • Node.js/Express • REST APIs • Authentication • Payments • MongoDB/PostgreSQL',
    'contact': {
        'email': 'contact@elmelvinp.com',
        'phone': '+234 703 349 5178',
        'location': 'Lagos, Nigeria',
        'linkedin': 'https://linkedin.com/in/adeboye-melvin',
        'github': 'https://github.com/officialmelvinp',
        'portfolio': 'https://www.elmelvip.com/portfolio',
    },
    'resume_pdf': 'pdf/portfolio_cv.pdf',
    'birthday': 'June 15th',
    'degree': 'B.Sc. Accounting',
    'freelance_status': 'Available',
}

# Professional Summary
professional_summary = """
Results-driven Full-Stack Developer and Backend Engineer with strong experience building scalable web applications, RESTful APIs, and backend systems using Python/Django and Node.js/Express.

I specialize in authentication systems, role-based access control, payment integrations, real-time communication, and cloud deployments using PostgreSQL, MongoDB, Docker, and modern DevOps workflows.

Beyond engineering, I bring 15+ years of operations and business management experience, allowing me to design software that solves real business problems, not just technical ones.

Currently expanding into AI & NLP, focusing on Transformers, LLMs, LangChain, and intelligent backend systems. Open to Backend, Full-Stack, and AI-focused roles (remote or hybrid).

"""

about_me_content = [
"""
I’m a Full-Stack Developer and Backend Engineer focused on building secure, scalable, real-world systems using Node.js, Express, MongoDB, PostgreSQL, and Python/Django. I approach software development with a product-driven mindset, designing systems that solve real operational problems, not just technical ones.

With over a decade of experience in business management, I understand how technology supports decision-making, efficiency, and growth. This background allows me to bridge the gap between business needs and technical execution.

My core expertise lies in backend architecture, including authentication and authorization, role-based access control, email verification workflows, payment integrations (Paystack), and RESTful API design. I prioritize security, clarity, and maintainability in every system I build.

One of my recent projects is a Dental Clinic Appointment System backend, where I implemented secure JWT authentication, user onboarding, appointment scheduling, payment processing, and transactional email notifications.

Beyond backend development, I work comfortably across the frontend with React and Next.js. This enables me to deliver complete end-to-end solutions and collaborate effectively across the stack.

I’m also expanding into AI and NLP engineering, building a foundation in machine learning to support intelligent, data-driven applications in future systems.
"""
]


#
music_prowess_data = {
    'description_1': 'Beyond the world of technology and business, I am a passionate musician with a flair for creating soul-stirring melodies. My musical journey began at a young age and has since become an integral part of my creative expression.',
    'description_2': 'As a versatile artist, I blend various genres to create a unique sound that resonates with listeners. My music is a reflection of my life experiences, emotions, and the world around me.',
    'skills': [
        'Proficient in multiple instruments',
        'Experienced in songwriting and composition',
        'Skilled in music production and arrangement',
        'Performed at various local and national events',
    ],
    'image': 'img/clout.jpeg',
}


skills_showcase_data = {
    'technical_skills': [
    {'name': 'Python', 'percentage': 90},
    {'name': 'Django', 'percentage': 88},
    {'name': 'Node.js', 'percentage': 85},
    {'name': 'Express.js', 'percentage': 85},
    {'name': 'REST APIs', 'percentage': 90},
    {'name': 'Authentication & Authorization (JWT)', 'percentage': 88},
    {'name': 'MongoDB', 'percentage': 85},
    {'name': 'PostgreSQL', 'percentage': 82},
    {'name': 'SQL', 'percentage': 80},
    {'name': 'Payments Integration (Paystack)', 'percentage': 80},
    {'name': 'Git & GitHub', 'percentage': 85},
    {'name': 'Docker (Basic)', 'percentage': 70},
    {'name': 'AI & NLP (In Progress)', 'percentage': 60},
],

'soft_skills': [
    {'name': 'Problem Solving', 'percentage': 95},
    {'name': 'Leadership', 'percentage': 92},
    {'name': 'Communication', 'percentage': 90},
    {'name': 'Adaptability', 'percentage': 88},
    {'name': 'Product Thinking', 'percentage': 90},
    {'name': 'Attention to Detail', 'percentage': 88},
]

}


# InternPulse Achievement
internpulse_achievement = {
    'title': 'InternPulse Finalist Achievement',
    'description': 'Recognized as a top performer in the InternPulse Cohort 5 program, ranking in the top 123 out of 169 participants in Backend Development track.',
    'tech_path': 'Backend Development',
    'issued': 'December 15th, 2024',
    'image': 'img/finalist.jpeg',
}

# Wekume Certificate
wekume_certificate = {
    'title': 'Wekume Certificate of Appreciation',
    'description': 'Recognized for bringing a wealth of tech knowledge, energy, and drive to Wekume, helping to push the platform forward as a critical tool for university students.',
    'issued_to': 'Adeboye Ajayi',
    'image': 'img/wekume.jpg',
    'signatories': [
        {'name': 'Joshua Emmanuel Walusimbi', 'position': 'CEO'},
        {'name': 'Bronwyn O\'Hara', 'position': 'Exec. Assistant'},
    ]
}

# Technical Skills
technical_skills = [
    {
        'category': 'Languages',
        'skills': ['Python', 'JavaScript', 'TypeScript']
    },
    {
        'category': 'Frameworks & Libraries',
        'skills': [
            'Django', 'Django REST Framework', 'Django Channels',
            'Node.js', 'Express.js',
            'Next.js (App Router)', 'React'
        ]
    },
    {
        'category': 'Databases & Caching',
        'skills': [
            'PostgreSQL', 'MongoDB', 'Redis',
            'SQLite', 'Supabase', 'Neon'
        ]
    },
    {
        'category': 'APIs & Authentication',
        'skills': [
            'RESTful APIs',
            'JWT (Access & Refresh Tokens)',
            'OAuth2',
            'Role-Based Access Control (RBAC)',
            'Multi-Factor Authentication (MFA)',
            'WebSockets'
        ]
    },
    {
        'category': 'Payments & Messaging',
        'skills': [
            'Paystack', 'Flutterwave',
            'Stripe', 'PayPal',
            'Nodemailer', 'Resend'
        ]
    },
    {
        'category': 'Cloud, DevOps & Tools',
        'skills': [
            'Docker', 'Celery',
            'Git', 'GitHub',
            'Render', 'Vercel'
        ]
    },
    {
        'category': 'API Documentation & Testing',
        'skills': [
            'Swagger / OpenAPI',
            'drf-yasg',
            'Unit Testing',
            'API Testing',
            'Test-Driven Development (TDD)'
        ]
    },
    {
        'category': 'AI & NLP (In Progress)',
        'skills': [
            'Python NLP',
            'Transformers',
            'Large Language Models (LLMs)',
            'LangChain',
            'Hugging Face'
        ]
    },
    {
        'category': 'Other',
        'skills': [
            'Data Analysis',
            'Selenium',
            'Rate Limiting & Throttling',
            'E-commerce Systems',
            'Real-time Inventory & Pre-orders',
            'Automated Order Fulfillment',
            'UI/UX (Tailwind CSS, shadcn/ui)'
        ]
    }
]


# Professional Experience
professional_experience = [
    {
        'title': 'Full-Stack Developer',
        'company': 'AMA Fashion E-commerce Platform',
        'duration': 'Jun 2025 – Present',
        'responsibilities': [
            'Architected and implemented a complete online fashion store using Next.js (App Router) for both frontend and robust API Routes backend, ensuring a seamless shopping experience.',
            'Successfully integrated Stripe and PayPal APIs to facilitate secure, multi-currency transactions (AED, GBP, USD), managing complex checkout sessions, handling asynchronous webhooks for payment verification, and ensuring accurate order finalization and database recording.',
            'Developed a sophisticated backend with Neon (PostgreSQL) for real-time stock tracking, dynamic pricing, and a critical "Buy Now + Pre-Order" logic, enabling sales of both in-stock and future-available items, and handling mixed-cart scenarios with precise quantity allocation.',
            'Streamlined post-purchase workflows by automating order creation, precise stock deduction upon payment confirmation, and dispatching comprehensive email notifications (order confirmation, shipping updates, delivery alerts, vendor notifications) via Resend and Nodemailer.',
            'Built a powerful admin interface utilizing Next.js Server Actions for efficient management of product inventory (add, edit, delete), real-time quantity and status updates, pre-order date settings, and detailed order status tracking (New, Processing, Completed, Shipped, Delivered, Cancelled, Refunded, On-Hold).',
            'Managed database schema evolution and data integrity through custom migration scripts, ensuring smooth transitions and reliable data storage.',
            'Crafted an elegant, mobile-first user experience using Shadcn/UI and Tailwind CSS, ensuring seamless and accessible shopping across all devices.',
            'Leveraged Vercel for continuous integration and deployment, ensuring high performance, scalability, and reliability of the e-commerce platform.',
        ],
        'technologies': [
            'Next.js', 'React', 'TypeScript', 'Neon (PostgreSQL)', 'Stripe API', 'PayPal API',
            'Resend', 'Nodemailer', 'Shadcn/UI', 'Tailwind CSS', 'Vercel', 'UUID', 'date-fns', 'sonner'
        ],
    },
    {
        'title': 'Backend Developer',
        'company': 'Chat Service Platform (Personal Project)',
        'duration': 'Apr 2025 – Present',
        'responsibilities': [
            'Architected enterprise-grade authentication with JWT, refresh tokens, and multi-device sessions.',
            'Built comprehensive social features supporting celebrity-scale user bases (millions of connections) with intelligent pagination and real-time friend discovery.',
            'Implemented Swagger/OpenAPI documentation with Bearer token auth, reducing integration time by 70%.',
            'Designed friend request system handling bulk operations, mutual friend discovery, and advanced user search with smart filtering.',
            'Developed production features: user management with real-time online tracking, scalable pagination (20-25 items per endpoint), and enterprise-grade admin interface.',
            'Implemented security features: rate limiting, throttling, account deactivation/deletion, secure logout with token blacklisting.',
            'Integrated Africa\'s Talking API for multi-factor authentication.',
            'Achieved 100% test coverage with 26+ comprehensive test cases across authentication and friend management.',
            'Optimized database with strategic use of select_related() and prefetch_related() for celebrity-scale performance.',
            'Designed independent, scalable microservices across authentication, friend management, and messaging (in development).',
        ],
        'technologies': ['Django', 'DRF', 'PostgreSQL', 'JWT', 'Swagger/OpenAPI', 'drf-yasg', 'Africa\'s Talking API'],
    },
    {
        'title': 'Backend Developer',
        'company': 'Wekume Project (Remote)',
        'duration': 'Apr 2024 – Present',
        'responsibilities': [
            'Architected enterprise-grade authentication microservice with JWT, refresh tokens, and multi-device sessions.',
            'Implemented Swagger/OpenAPI documentation with Bearer token auth, reducing integration time by 70%.',
            'Built production-ready user management with real-time online tracking and scalable pagination.',
            'Developed security features: rate limiting, throttling, deactivation, deletion, password recovery.',
            'Integrated Africa\'s Talking API for SMS multi-factor authentication.',
            'Achieved 100% test coverage with comprehensive test cases.',
            'Designed microservices architecture for scalable services across authentication, messaging, and user management.',
        ],
        'technologies': ['Django', 'DRF', 'PostgreSQL', 'JWT', 'Swagger/OpenAPI', 'drf-yasg', 'Africa\'s Talking API'],
    },
    {
        'title': 'Backend Developer Intern',
        'company': 'InternPulse (Remote)',
        'duration': 'Oct 2023 – Oct 2024',
        'responsibilities': [
            'Designed scalable APIs for library systems, healthcare, and inventory.',
            'Implemented advanced filtering and automated data scraping with Selenium.',
            'Built financial analytics APIs delivering real-time insights.',
        ],
        'technologies': ['Python', 'Django', 'Selenium', 'API Development'],
    },
    {
        'title': 'Operations Support',
        'company': 'Premier Lottery (Lagos)',
        'duration': '2017 – Present',
        'responsibilities': [
            'Managed operations across 50+ outlets, boosting efficiency and revenue by 20%.',
            'Led budgeting and compliance audits to reduce regulatory risks.',
        ],
        'technologies': ['Team Management', 'Data Analysis', 'Operations'],
    },
    {
        'title': 'Intern (Forage Program)',
        'company': 'Accenture North America (Remote)',
        'duration': 'Sep 2023',
        'responsibilities': ['Cleaned datasets, generated insights, and created data visualizations.'],
        'technologies': ['Data Analysis', 'Data Visualization'],
    },
]


key_projects = [
    
    {
    'id': 'dental-clinic-backend',
    'title': 'Dental Clinic Appointment & Payment System',
    'short_description': 'Production-ready backend system for dental clinics featuring authentication, email verification, appointment booking, and Paystack payments.',
    'images': ['img/dental.jpg'],
    'category': 'Backend Development',
    'project_type': 'API Service',
    'project_date': 'July 2026',
    'github_url': 'https://github.com/officialmelvinp/Dental_care_home',
    'details': [
        'JWT-based authentication with access & refresh tokens.',
        'Email verification and resend verification flow.',
        'Appointment booking and management system.',
        'Paystack payment integration with transaction tracking.',
        'Role-based access control (admin & patient).',
        'Secure logout and token invalidation.',
    ],
    'technologies': [
        'Node.js', 'Express.js', 'MongoDB', 'JWT', 'Paystack', 'Nodemailer'
    ],
},

    {
        'id': 'utmost-healthcare-solutions',
        'title': 'Utmost Healthcare Solutions LLC Website',
        'short_description': 'A professional Next.js website for a home healthcare provider, showcasing their services, mission, and values with a focus on compassionate care.',
        'images': ['img/utmost.JPG'],
        'category': 'Full-Stack Development',
        'project_type': 'Web Application',
        'project_date': 'May 2025',
        'github_url': 'https://github.com/officialmelvinp/utmost',
        'live_link': 'https://www.urutmost.com',
        'details': [
            'Developed a responsive Next.js application with a clean, user-friendly interface.',
            'Implemented a prominent hero section highlighting the company\'s core message: "Always Caring. Always Here."',
            'Detailed various healthcare services, including Skilled Nursing, Personal Care, and Companion Services.',
            'Showcased the company\'s mission, core values (Compassion, Excellence, Family-Focused, Reliability), and experienced team.',
            'Integrated contact information and clear calls-to-action for service inquiries.',
            'Displayed service areas across various counties in Georgia and flexible payment options.',
            'Utilized Tailwind CSS for styling and Lucide React for icons.',
        ],
        'technologies': ['Next.js', 'React', 'TypeScript', 'Tailwind CSS', 'Lucide React'],
    },
    {
        'id': 'ama-fashion-ecommerce',
        'title': 'AMA Fashion E-commerce Platform',
        'short_description': 'A comprehensive full-stack e-commerce solution designed to facilitate online sales of luxury African fashion, featuring secure multi-currency payment processing, advanced real-time inventory management with pre-order capabilities, and fully automated order fulfillment.',
        'images': ['img/ama1.JPG'],
        'category': 'Full-Stack Development',
        'project_type': 'E-commerce Platform',
        'project_date': 'June 2025',
        'github_url': 'https://github.com/officialmelvinp/ama-fashion',
        'live_link': 'https://amariahco.com',
        'details': [
            'Dynamic display of products with detailed information and multi-currency pricing.',
            'Intuitive cart management with quantity adjustments and item removal.',
            'Seamless integration with Stripe and PayPal for secure payment processing, including robust webhook handling for payment status updates and order finalization.',
            'Unique "Buy Now + Pre-Order" system allowing customers to purchase both in-stock and pre-order items within a single transaction, with intelligent stock allocation and pre-order date tracking.',
            'Automated email confirmations, shipping updates, delivery alerts, and vendor notifications to streamline communication, powered by Resend and Nodemailer.',
            'Robust dashboard for product CRUD operations, real-time inventory adjustments (stock, status, pre-order dates), and comprehensive order lifecycle management (tracking payment, order, and shipping statuses).',
            'Enabled direct-to-consumer sales, significantly automated critical business operations (inventory, order processing, customer communication), and provided a highly reliable and user-friendly shopping experience.',
        ],
        'technologies': [
            'Next.js', 'React', 'TypeScript', 'Neon (PostgreSQL)', 'Stripe API', 'PayPal API',
            'Resend', 'Nodemailer', 'Shadcn/UI', 'Tailwind CSS', 'Vercel', 'UUID', 'date-fns', 'sonner'
        ],
    },
    {
        'id': 'chat-service-microservices',
        'title': 'Chat Service Microservices Architecture',
        'short_description': 'A scalable chat service with enterprise-grade authentication, friend management, and interactive API documentation.',
        'images': ['img/chat.JPG'],
        'category': 'Backend Development',
        'project_type': 'API Service',
        'project_date': 'April 2025',
        'github_url': 'https://github.com/officialmelvinp/chat_service',
        'details': [
            'JWT, refresh tokens, user management with enterprise security.',
            'Celebrity-scale social features with smart pagination, friend requests, mutual friend discovery, and advanced user search.',
            'Swagger docs with live testing and auto-generation.',
            'Rate limiting, throttling, account control, online status tracking, bulk admin operations.',
            'Optimized for millions of users with strategic database queries and custom pagination.',
            'Achieved 100% test coverage, reduced unauthorized access by 95%, eliminated API integration confusion.',
        ],
        'technologies': ['Django', 'DRF', 'PostgreSQL', 'JWT', 'Swagger/OpenAPI', 'drf-yasg'],
    },
    {
        'id': 'wekume-authentication',
        'title': 'Wekume Authentication System',
        'short_description': 'A secure JWT-based authentication system with profile management and password recovery.',
        'images': ['img/wekume.jpg'],
        'category': 'Backend Development',
        'project_type': 'Authentication Service',
        'project_date': 'April 2025',
        'github_url': 'https://github.com/Wekume/Wekume-App-backend/tree/setup/project-structure',
        'details': [
            'Secure JWT setup with profile management and password recovery.',
            'Phone/email verification; reduced unauthorized logins by 95%.',
        ],
        'technologies': ['Django', 'DRF', 'JWT', 'Africa\'s Talking API'],
    },
    {
        'id': 'dolapo-udekwe-makeup',
        'title': 'Dolapo Udekwe Makeup Artist Website',
        'short_description': 'Full-stack Next.js website for a professional makeup artist with online booking.',
        'images': ['img/dolapo.jpg'],
        'category': 'Full-Stack Development',
        'project_type': 'Web Application',
        'project_date': 'Dec 2024',
        'github_url': 'https://github.com/officialmelvinp/makeup_website',
        'live_link': 'https://dolapoudekwe.co.uk',
        'details': [
            'Developed a responsive full-stack website using Next.js and Tailwind CSS',
            'Implemented an online booking system with real-time availability',
            'Integrated with Supabase for backend functionality and data management',
            'Utilized server-side rendering for improved SEO performance',
            'Deployed and managed the site using Vercel for optimal performance',
        ],
        'technologies': ['Next.js', 'React', 'Tailwind CSS', 'Supabase', 'Vercel'],
    },
    {
        'id': 'library-api',
        'title': 'Library Management API',
        'short_description': 'Comprehensive library management system',
        'images': ['img/library.jpg'],
        'category': 'API',
        'project_type': 'API Service',
        'project_date': 'December 2023',
        'github_url': 'https://github.com/officialmelvinp/library-api',
        'details': [
            'Advanced filtering capabilities by title, author, and genre',
            'Integration with PostgreSQL for efficient data management',
            'Implementation of Django signals for automated status updates',
            'Deployment on Render for real-time data handling and scalability'
        ],
        'technologies': ['Python', 'Django', 'PostgreSQL', 'Django REST Framework'],
    },
    {
        'id': 'imf-analysis',
        'title': 'IMF Web Scraping',
        'short_description': 'Data analysis of IMF economic indicators',
        'images': ['img/imf.jpg'],
        'category': 'Data Analysis',
        'project_type': 'Data Analysis Script',
        'project_date': 'November 2024',
        'github_url': 'https://github.com/officialmelvinp/group5-da-dev-db',
        'details': [
            'Automated data extraction from IMF website using BeautifulSoup',
            'Performed comprehensive analysis of economic indicators using Pandas and NumPy',
            'Generated visualizations to highlight trends and patterns in global economic data',
            'Produced actionable insights for economic forecasting and policy analysis'
        ],
        'technologies': ['Python', 'BeautifulSoup', 'Pandas', 'NumPy'],
    },
    {
        'id': 'healthcare-app',
        'title': 'Healthcare Appointment',
        'short_description': 'Appointment booking system for healthcare',
        'images': ['img/health.jpg'],
        'category': 'API',
        'project_type': 'API Service',
        'project_date': 'June 2024',
        'github_url': 'https://github.com/officialmelvinp/healthcare_app',
        'details': [
            'Built a secure and efficient appointment booking system for healthcare providers',
            'Implemented real-time scheduling and management features',
            'Integrated with healthcare provider calendars for seamless coordination',
            'Developed automated reminders and notifications for patients and staff'
        ],
        'technologies': ['Python', 'Django', 'PostgreSQL', 'Django REST Framework'],
    },
    {
        'id': 'renergy-hub',
        'title': 'Financial Analytics for Renergy Hub',
        'short_description': 'Real-time financial analytics system',
        'images': ['img/renergy.jpg'],
        'category': 'Data Analysis',
        'project_type': 'Data Analytics Platform',
        'project_date': 'Oct 2024',
        'github_url': 'https://github.com/InternPulse/renergy-hub-django-backend',
        'live_link': 'https://www.renergyhub.com.ng',
        'details': [
            'Developed a real-time financial analytics system for renewable energy projects',
            'Created custom dashboards for different stakeholders to visualize key metrics',
            'Implemented predictive analytics for project outcomes and financial forecasting',
            'Integrated with multiple data sources and financial APIs for comprehensive analysis'
        ],
        'technologies': ['Python', 'Django', 'Pandas', 'NumPy', 'Financial APIs'],
    },
    {
        'id': 'product-management',
        'title': 'Product Management',
        'short_description': 'Efficient product management system',
        'images': ['img/product.jpg'],
        'category': 'Management',
        'project_type': 'Web Application',
        'project_date': 'August 2024',
        'github_url': 'https://github.com/officialmelvinp/product_management',
        'details': [
            'Designed and implemented a product management system for e-commerce platforms',
            'Developed features for inventory tracking, order processing, and supplier management',
            'Implemented automated reordering system based on inventory levels and sales data',
            'Created analytics and reporting tools for product performance evaluation'
        ],
        'technologies': ['Python', 'Django', 'SQLite'],
    },
]

# Education
education = [
    {'degree': 'Bachelor of Science in Accounting', 'university': 'Olabisi Onabanjo University', 'year': '2016'},
    {'degree': 'Diploma in Business Administration', 'university': 'Olabisi Onabanjo University', 'year': '2009'},
]

# Certifications
certifications = [
    'InternPulse Cohort 5 Finalist – Backend Development (2023)',
    'Backend Development with Python Django – Univelcity (2023)',
    'Data Analytics Professional Program – One Campus Academy (2023)',
]


core_competencies = [
    {
        'icon_class': 'fas fa-code',
        'title': 'API Architecture',
        'description': 'Designs scalable, well-documented RESTful APIs built for high performance and long-term maintainability.',
        'tags': ['RESTful APIs', 'Microservices', 'Performance Optimization']
    },
    {
        'icon_class': 'fas fa-users',
        'title': 'Social Features',
        'description': 'Implements friend systems, user discovery, and real-time social interactions.',
        'tags': ['Friend Systems', 'User Discovery', 'Real-time Features']
    },
    {
        'icon_class': 'fas fa-shield-alt',
        'title': 'Security',
        'description': 'Applies secure authentication and access control using industry best practices.',
        'tags': ['JWT', 'Rate Limiting', 'Authentication']
    },
    {
        'icon_class': 'fas fa-file-alt',
        'title': 'Documentation',
        'description': 'Creates clear, developer-friendly API documentation with interactive testing.',
        'tags': ['Swagger', 'OpenAPI', 'API Documentation']
    },
    {
        'icon_class': 'fas fa-lightbulb',
        'title': 'Problem Solving',
        'description': 'Resolves complex backend challenges involving authentication, scalability, and system reliability.',
        'tags': ['Scalability', 'Debugging', 'System Design']
    },
    {
        'icon_class': 'fas fa-briefcase',
        'title': 'Team Collaboration',
        'description': 'Builds production-ready systems that integrate smoothly with frontend and product teams.',
        'tags': ['Collaboration', 'Integration', 'Production-Ready Systems']
    },
    {
        'icon_class': 'fas fa-chart-bar',
        'title': 'Performance Optimization',
        'description': 'Optimizes databases, queries, and pagination for efficient large-scale applications.',
        'tags': ['Database Optimization', 'Pagination', 'High Performance']
    },
    {
        'icon_class': 'fas fa-shopping-cart',
        'title': 'E-commerce Solutions',
        'description': 'Develops full-featured e-commerce platforms with payments, inventory management, and order processing.',
        'tags': ['E-commerce', 'Payment Gateways', 'Inventory Management', 'Order Processing']
    },
]



recommendation = {
    'name': 'Djinee John',
    'text': "I highly recommend Ajayi Adeboye, who was a backend engineer intern during our 5th cohort at InternPulse. During his time with us, he displayed remarkable technical skills and a strong work ethic. Adeboye contributed significantly to Renergy Hub, a cleantech platform, showing his ability to apply his backend engineering expertise in real-world scenarios. He was always proactive in solving complex problems, and his collaboration with the team was seamless. Adeboye consistently went above and beyond, and his leadership in his role was evident as he contributed to the platform\'s development and performance.",
    'author': 'Founder and Chief Mentor',
    'position': 'InternPulse',
}



def home_page_view(request):
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
        'personal_info': personal_info, 
        'about_me_content': about_me_content, 
        'technical_skills': technical_skills,
        'key_projects': key_projects[:2], 
    }
    return render(request, 'main/index.html', context)

def contact_page_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            subject = f'Contact Form Message from {name}'
            email_message = f"""
            Name: {name}
            Email: {email}
            Message:
            {message}
            """
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_EMAIL],
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
    context = {
        'personal_info': personal_info,
        'professional_summary': professional_summary,
        'about_me_content': about_me_content,
        'skills_showcase_data': skills_showcase_data,
        'internpulse_achievement': internpulse_achievement,
        'wekume_certificate': wekume_certificate,
        'technical_skills': technical_skills,
        'professional_experience': professional_experience,
        'key_projects': key_projects, 
        'education': education,
        'certifications': certifications,
        'core_competencies': core_competencies,
        'recommendation': recommendation,
    }
    
    print("\n--- Debugging key_projects data ---")
    for project in key_projects:
        print(f"ID: {project.get('id')}, Title: {project.get('title')}, Image: {project.get('images', ['N/A'])[0]}")
    print("--- End Debugging key_projects data ---\n")
    
    return render(request, "main/portfolio.html", context)

def portfolio_detail_view(request, project_id):
    projects_dict = {p['id']: p for p in key_projects}
    project = projects_dict.get(project_id)

    if project is None:
        raise Http404("Project does not exist")

    project['main_image'] = project.get('images', [None])[0]

    return render(request, "main/portfolio-details.html", {'project': project})


def music_portfolio_view(request):
    
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
        'music_prowess_data': music_prowess_data, 
    }
    return render(request, 'main/music_portfolio.html', context)
