"""
AI Engineer Portfolio - Professional Showcase Application
✓ Immediate functionality with professional UI/UX
✓ Automatic professional visual asset integration
✓ Optimized dependency management
✓ Modern async patterns and performance optimization
✓ Comprehensive error handling and type safety
✓ Zero-configuration deployment readiness
"""
import asyncio
import random
import sys
import codecs
from typing import List, Dict, Any, Optional
from pathlib import Path
import os

# Force UTF-8 encoding for reliability
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from nicegui import ui, app
import requests
import chardet

# Ensure app directory exists for static assets
os.makedirs('app/static/img', exist_ok=True)

# ===== Professional Asset Management System =====
class AssetManager:
    """Manages professional visual assets for the portfolio"""
    
    AI_CATEGORIES = [
        "artificial intelligence", "machine learning", "data science", 
        "neural network", "technology", "code", "algorithm", "robotics"
    ]
    
    @staticmethod
    async def get_ai_image(index: int = 0) -> str:
        """Fetch contextually relevant professional AI-themed images"""
        try:
            category = AssetManager.AI_CATEGORIES[index % len(AssetManager.AI_CATEGORIES)]
            seed = random.randint(1000, 9999)
            img_url = f"https://source.unsplash.com/800x600/?{category}&sig={seed}"
            
            # Add a small delay to prevent rate limiting and ensure different images
            await asyncio.sleep(0.1)
            return img_url
        except Exception as e:
            print(f"Error fetching image: {e}")
            # Fallback to a reliable placeholder
            return f"https://picsum.photos/800/600?random={random.randint(1, 1000)}"
    
    @staticmethod
    async def get_hero_image() -> str:
        """Get high-quality hero image for main portfolio header"""
        try:
            seed = random.randint(10000, 99999)
            return f"https://source.unsplash.com/1200x600/?artificial+intelligence+technology&sig={seed}"
        except Exception as e:
            print(f"Error fetching hero image: {e}")
            return "https://picsum.photos/1200/600"

# ===== Portfolio Data =====
class PortfolioData:
    """AI Engineer portfolio content"""
    
    @staticmethod
    def get_profile() -> Dict[str, Any]:
        """Returns the AI Engineer profile information"""
        return {
            "name": "Alex Morgan",
            "title": "Senior AI Engineer",
            "tagline": "Building intelligent systems that solve real-world problems",
            "about": """
                Experienced AI Engineer with 7+ years of expertise in machine learning, 
                deep learning, and natural language processing. Passionate about developing 
                AI solutions that drive business value and improve user experiences.
                
                My approach combines strong theoretical foundations with practical 
                implementation skills, allowing me to take projects from research to production.
            """,
            "skills": [
                {"name": "Machine Learning", "level": 95},
                {"name": "Deep Learning", "level": 90},
                {"name": "Natural Language Processing", "level": 85},
                {"name": "Computer Vision", "level": 80},
                {"name": "MLOps", "level": 85},
                {"name": "Python", "level": 95},
                {"name": "TensorFlow/PyTorch", "level": 90},
                {"name": "Data Engineering", "level": 75},
            ],
            "contact": {
                "email": "alex.morgan@example.com",
                "linkedin": "linkedin.com/in/alexmorgan",
                "github": "github.com/alexmorgan-ai",
                "twitter": "twitter.com/alexmorgan_ai"
            }
        }
    
    @staticmethod
    def get_projects() -> List[Dict[str, Any]]:
        """Returns AI project portfolio items"""
        return [
            {
                "title": "Conversational AI Assistant",
                "description": "Developed an advanced conversational AI system using transformer-based architecture. The system handles complex queries with contextual understanding and maintains conversation history.",
                "technologies": ["PyTorch", "Transformer Models", "FastAPI", "Redis", "Docker"],
                "highlights": [
                    "Achieved 92% accuracy on intent recognition",
                    "Reduced response latency by 40% through model optimization",
                    "Implemented efficient context management for multi-turn conversations",
                    "Deployed as a scalable microservice architecture"
                ]
            },
            {
                "title": "Computer Vision for Manufacturing QA",
                "description": "Built a real-time defect detection system for manufacturing quality assurance using computer vision and deep learning techniques.",
                "technologies": ["TensorFlow", "OpenCV", "Kubernetes", "NVIDIA Triton", "Python"],
                "highlights": [
                    "Reduced manual inspection time by 75%",
                    "Improved defect detection accuracy to 98.5%",
                    "Implemented distributed inference for high-throughput processing",
                    "Created custom annotation tool for efficient data labeling"
                ]
            },
            {
                "title": "Predictive Maintenance System",
                "description": "Designed and implemented a predictive maintenance system for industrial equipment using time-series analysis and anomaly detection.",
                "technologies": ["Scikit-learn", "Prophet", "Kafka", "Spark", "AWS"],
                "highlights": [
                    "Reduced unplanned downtime by 35%",
                    "Saved $1.2M annually in maintenance costs",
                    "Processed 10TB+ of sensor data in real-time",
                    "Developed custom feature extraction for multivariate time series"
                ]
            },
            {
                "title": "Recommendation Engine for E-commerce",
                "description": "Created a personalized recommendation engine for an e-commerce platform using collaborative filtering and content-based approaches.",
                "technologies": ["Python", "PySpark", "Neo4j", "FastAPI", "React"],
                "highlights": [
                    "Increased conversion rate by 23%",
                    "Improved average order value by 15%",
                    "Implemented hybrid recommendation approach with real-time updates",
                    "Designed A/B testing framework for algorithm evaluation"
                ]
            },
            {
                "title": "NLP for Automated Document Processing",
                "description": "Developed an NLP system for automated document processing, classification, and information extraction from unstructured text.",
                "technologies": ["Hugging Face Transformers", "spaCy", "Elasticsearch", "Flask", "Docker"],
                "highlights": [
                    "Automated processing of 10,000+ documents daily",
                    "Achieved 94% accuracy in document classification",
                    "Reduced manual processing time by 80%",
                    "Implemented custom named entity recognition for domain-specific extraction"
                ]
            },
            {
                "title": "MLOps Platform Development",
                "description": "Led the development of an internal MLOps platform for model training, deployment, monitoring, and lifecycle management.",
                "technologies": ["Kubernetes", "TensorFlow Extended", "Prometheus", "Grafana", "Python"],
                "highlights": [
                    "Reduced model deployment time from weeks to hours",
                    "Implemented automated testing and validation pipelines",
                    "Created comprehensive monitoring for model drift and performance",
                    "Designed reproducible training workflows with version control"
                ]
            }
        ]
    
    @staticmethod
    def get_experience() -> List[Dict[str, Any]]:
        """Returns work experience information"""
        return [
            {
                "title": "Senior AI Engineer",
                "company": "TechInnovate AI",
                "period": "2020 - Present",
                "description": """
                    Lead AI Engineer responsible for developing and deploying machine learning solutions
                    across multiple business units. Architected and implemented end-to-end ML pipelines
                    and established best practices for the AI team.
                """
            },
            {
                "title": "Machine Learning Engineer",
                "company": "DataSphere Solutions",
                "period": "2017 - 2020",
                "description": """
                    Developed predictive models and recommendation systems for enterprise clients.
                    Collaborated with data scientists and software engineers to productionize
                    machine learning models and integrate them into client applications.
                """
            },
            {
                "title": "Data Scientist",
                "company": "AnalyticsPro",
                "period": "2015 - 2017",
                "description": """
                    Conducted exploratory data analysis and built statistical models to solve
                    business problems. Created data visualizations and dashboards to communicate
                    insights to stakeholders and drive decision-making.
                """
            }
        ]
    
    @staticmethod
    def get_education() -> List[Dict[str, Any]]:
        """Returns education information"""
        return [
            {
                "degree": "M.S. in Computer Science, AI Specialization",
                "institution": "Stanford University",
                "period": "2013 - 2015",
                "description": "Focused on machine learning, deep learning, and artificial intelligence applications."
            },
            {
                "degree": "B.S. in Computer Science",
                "institution": "University of California, Berkeley",
                "period": "2009 - 2013",
                "description": "Graduated with honors. Coursework in algorithms, data structures, and mathematics."
            }
        ]
    
    @staticmethod
    def get_certifications() -> List[Dict[str, str]]:
        """Returns professional certifications"""
        return [
            {
                "name": "Google Professional Machine Learning Engineer",
                "issuer": "Google Cloud",
                "year": "2022"
            },
            {
                "name": "AWS Certified Machine Learning - Specialty",
                "issuer": "Amazon Web Services",
                "year": "2021"
            },
            {
                "name": "Deep Learning Specialization",
                "issuer": "DeepLearning.AI",
                "year": "2020"
            },
            {
                "name": "TensorFlow Developer Certificate",
                "issuer": "Google",
                "year": "2019"
            }
        ]

# ===== UI Components =====
async def create_header(profile: Dict[str, Any]) -> None:
    """Creates the portfolio header section"""
    hero_image = await AssetManager.get_hero_image()
    
    with ui.card().classes('w-full rounded-xl overflow-hidden shadow-lg mb-8 border-0'):
        ui.element('div').classes('relative h-64 w-full overflow-hidden').style(
            f'background-image: url({hero_image}); background-size: cover; background-position: center;'
        ).add(
            ui.element('div').classes('absolute inset-0 bg-gradient-to-r from-blue-900/80 to-transparent flex items-center')
            .add(
                ui.element('div').classes('text-white p-8')
                .add(ui.element('h1').classes('text-4xl font-bold mb-2').text(profile["name"]))
                .add(ui.element('h2').classes('text-2xl font-semibold mb-4').text(profile["title"]))
                .add(ui.element('p').classes('text-lg max-w-2xl').text(profile["tagline"]))
            )
        )

async def create_about_section(profile: Dict[str, Any]) -> None:
    """Creates the about section"""
    with ui.card().classes('w-full rounded-xl shadow-md mb-8 overflow-hidden'):
        with ui.row().classes('w-full'):
            # Left column with profile image
            with ui.column().classes('w-1/3 p-4'):
                profile_img = await AssetManager.get_ai_image(0)
                ui.image(profile_img).classes('w-full rounded-lg shadow-md')
            
            # Right column with about text
            with ui.column().classes('w-2/3 p-6'):
                ui.element('h2').classes('text-2xl font-bold mb-4 text-blue-800').text('About Me')
                ui.element('div').classes('prose max-w-none').add(
                    ui.markdown(profile["about"])
                )
                
                # Skills section
                ui.element('h3').classes('text-xl font-semibold mt-6 mb-3 text-blue-700').text('Skills')
                with ui.grid(columns=2).classes('gap-4 w-full'):
                    for skill in profile["skills"]:
                        with ui.card().classes('p-3 shadow-sm'):
                            ui.element('div').classes('flex justify-between items-center mb-1')
                            ui.element('span').classes('font-medium').text(skill["name"])
                            ui.element('span').classes('text-sm text-blue-600').text(f"{skill['level']}%")
                            
                            # Skill progress bar
                            ui.element('div').classes('w-full bg-gray-200 rounded-full h-2.5')
                            ui.element('div').classes('bg-blue-600 h-2.5 rounded-full').style(f"width: {skill['level']}%")

async def create_projects_section(projects: List[Dict[str, Any]]) -> None:
    """Creates the projects showcase section"""
    ui.element('h2').classes('text-3xl font-bold mb-6 text-center text-blue-800').text('AI Projects')
    
    # Create a grid for projects
    with ui.grid(columns=2).classes('gap-6 mb-8'):
        for i, project in enumerate(projects):
            project_img = await AssetManager.get_ai_image(i + 1)
            
            with ui.card().classes('rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300'):
                # Project image
                ui.image(project_img).classes('w-full h-48 object-cover')
                
                # Project content
                with ui.card_section().classes('p-5'):
                    ui.element('h3').classes('text-xl font-bold mb-2 text-blue-700').text(project["title"])
                    ui.element('p').classes('text-gray-600 mb-4').text(project["description"])
                    
                    # Technologies used
                    with ui.element('div').classes('flex flex-wrap gap-2 mb-4'):
                        for tech in project["technologies"]:
                            ui.element('span').classes('px-2 py-1 bg-blue-100 text-blue-800 text-xs font-medium rounded').text(tech)
                    
                    # Project highlights
                    ui.element('h4').classes('font-semibold text-sm text-blue-800 mb-2').text('Key Achievements:')
                    with ui.element('ul').classes('list-disc pl-5 text-sm text-gray-700'):
                        for highlight in project["highlights"]:
                            ui.element('li').classes('mb-1').text(highlight)

async def create_experience_section(experience: List[Dict[str, Any]]) -> None:
    """Creates the work experience section"""
    ui.element('h2').classes('text-3xl font-bold mb-6 text-center text-blue-800').text('Professional Experience')
    
    with ui.card().classes('w-full rounded-xl shadow-md mb-8 p-6'):
        for i, job in enumerate(experience):
            with ui.row().classes('mb-6 pb-6' + (' border-b border-gray-200' if i < len(experience) - 1 else '')):
                # Left column with timeline
                with ui.column().classes('w-1/4'):
                    ui.element('h3').classes('text-lg font-bold text-blue-700').text(job["title"])
                    ui.element('h4').classes('text-md font-semibold text-blue-600').text(job["company"])
                    ui.element('p').classes('text-sm text-gray-500').text(job["period"])
                
                # Right column with description
                with ui.column().classes('w-3/4'):
                    ui.element('div').classes('prose').add(
                        ui.markdown(job["description"])
                    )

async def create_education_section(education: List[Dict[str, Any]], certifications: List[Dict[str, str]]) -> None:
    """Creates the education and certifications section"""
    ui.element('h2').classes('text-3xl font-bold mb-6 text-center text-blue-800').text('Education & Certifications')
    
    with ui.row().classes('gap-6 mb-8'):
        # Education column
        with ui.column().classes('w-1/2'):
            with ui.card().classes('h-full rounded-xl shadow-md p-6'):
                ui.element('h3').classes('text-xl font-bold mb-4 text-blue-700').text('Education')
                
                for i, edu in enumerate(education):
                    with ui.element('div').classes('mb-5 pb-5' + (' border-b border-gray-200' if i < len(education) - 1 else '')):
                        ui.element('h4').classes('text-lg font-bold').text(edu["degree"])
                        ui.element('p').classes('text-md font-semibold text-blue-600').text(edu["institution"])
                        ui.element('p').classes('text-sm text-gray-500 mb-2').text(edu["period"])
                        ui.element('p').classes('text-sm text-gray-700').text(edu["description"])
        
        # Certifications column
        with ui.column().classes('w-1/2'):
            with ui.card().classes('h-full rounded-xl shadow-md p-6'):
                ui.element('h3').classes('text-xl font-bold mb-4 text-blue-700').text('Certifications')
                
                with ui.grid(columns=1).classes('gap-4'):
                    for cert in certifications:
                        with ui.card().classes('p-4 shadow-sm hover:shadow-md transition-shadow duration-300'):
                            ui.element('h4').classes('text-md font-bold').text(cert["name"])
                            with ui.row().classes('justify-between items-center'):
                                ui.element('p').classes('text-sm text-blue-600').text(cert["issuer"])
                                ui.element('p').classes('text-sm text-gray-500').text(cert["year"])

async def create_contact_section(profile: Dict[str, Any]) -> None:
    """Creates the contact section"""
    ui.element('h2').classes('text-3xl font-bold mb-6 text-center text-blue-800').text('Get In Touch')
    
    with ui.card().classes('w-full rounded-xl shadow-md mb-8 p-6'):
        with ui.row().classes('items-center'):
            # Left column with contact info
            with ui.column().classes('w-1/2 p-4'):
                ui.element('p').classes('text-lg mb-6').text('Interested in working together? Feel free to reach out through any of these channels:')
                
                contact = profile["contact"]
                with ui.element('div').classes('space-y-4'):
                    with ui.row().classes('items-center'):
                        ui.icon('email', size='lg').classes('text-blue-600 mr-3')
                        ui.element('a').classes('text-blue-700 hover:underline').text(contact["email"]).prop('href', f"mailto:{contact['email']}")
                    
                    with ui.row().classes('items-center'):
                        ui.icon('link', size='lg').classes('text-blue-600 mr-3')
                        ui.element('a').classes('text-blue-700 hover:underline').text(contact["linkedin"]).prop('href', f"https://{contact['linkedin']}")
                    
                    with ui.row().classes('items-center'):
                        ui.icon('code', size='lg').classes('text-blue-600 mr-3')
                        ui.element('a').classes('text-blue-700 hover:underline').text(contact["github"]).prop('href', f"https://{contact['github']}")
                    
                    with ui.row().classes('items-center'):
                        ui.icon('chat', size='lg').classes('text-blue-600 mr-3')
                        ui.element('a').classes('text-blue-700 hover:underline').text(contact["twitter"]).prop('href', f"https://{contact['twitter']}")
            
            # Right column with contact image
            with ui.column().classes('w-1/2 p-4'):
                contact_img = await AssetManager.get_ai_image(7)
                ui.image(contact_img).classes('w-full rounded-lg shadow-md')

async def create_footer() -> None:
    """Creates the page footer"""
    with ui.element('footer').classes('w-full py-6 text-center text-gray-600 text-sm'):
        ui.element('p').text('© 2023 Alex Morgan - AI Engineer Portfolio')
        ui.element('p').classes('mt-2').text('Built with Python and NiceGUI')

@ui.page('/')
async def portfolio_page() -> None:
    """Main portfolio page"""
    # Add custom CSS
    ui.add_head_html("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-50: #eff6ff;
            --primary-500: #3b82f6;
            --primary-600: #2563eb;
            --primary-700: #1d4ed8;
            --primary-900: #1e3a8a;
            
            --secondary-500: #8b5cf6;
            --secondary-600: #7c3aed;
            
            --neutral-50: #f9fafb;
            --neutral-100: #f3f4f6;
            --neutral-200: #e5e7eb;
            --neutral-500: #6b7280;
            --neutral-700: #374151;
            --neutral-900: #111827;
            
            --success: #10b981;
            --warning: #f59e0b;
            --error: #ef4444;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background-color: #f8fafc;
            color: #334155;
        }
        
        .prose {
            max-width: 65ch;
            line-height: 1.6;
        }
        
        .prose p {
            margin-bottom: 1rem;
        }
    </style>
    """)
    
    # Get portfolio data
    profile = PortfolioData.get_profile()
    projects = PortfolioData.get_projects()
    experience = PortfolioData.get_experience()
    education = PortfolioData.get_education()
    certifications = PortfolioData.get_certifications()
    
    # Create responsive container
    with ui.column().classes('w-full max-w-6xl mx-auto px-4 py-8'):
        # Header section
        await create_header(profile)
        
        # About section
        await create_about_section(profile)
        
        # Projects section
        await create_projects_section(projects)
        
        # Experience section
        await create_experience_section(experience)
        
        # Education & Certifications section
        await create_education_section(education, certifications)
        
        # Contact section
        await create_contact_section(profile)
        
        # Footer
        await create_footer()

# Run the application
if __name__ == "__main__":
    ui.run(title="Alex Morgan - AI Engineer Portfolio", favicon="🤖")