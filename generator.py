#!/usr/bin/env python3
"""
Personal Homepage Generator V2 - Template-based
Generates a static personal homepage from markdown content using Jinja2 templates
"""

import os
import json
import yaml
import markdown
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import shutil
from jinja2 import Environment, FileSystemLoader


class PersonalHomepageGenerator:
    def __init__(self, content_dir: str = "content", output_dir: str = "dist", template_dir: str = "templates"):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = Path(template_dir)
        
        # Initialize Jinja2
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        
        # Initialize markdown parser with extensions
        self.md = markdown.Markdown(extensions=[
            'extra',
            'meta',
            'toc',
            'tables',
            'fenced_code',
            'codehilite'
        ])
        
        # Data storage
        self.author_data = {}
        self.publications = []
        self.projects = []
        self.config = {}
    
    def parse_frontmatter(self, content: str) -> tuple[dict, str]:
        """Extract YAML frontmatter and content from markdown file"""
        if content.startswith('---'):
            try:
                parts = content.split('---', 2)[1:]
                if len(parts) == 2:
                    frontmatter = yaml.safe_load(parts[0])
                    body = parts[1].strip()
                    return frontmatter or {}, body
            except:
                pass
        return {}, content
    
    def read_markdown_file(self, filepath: Path) -> dict:
        """Read and parse a markdown file with frontmatter"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        meta, body = self.parse_frontmatter(content)
        meta['content_html'] = self.md.convert(body)
        meta['content_raw'] = body
        
        return meta
    
    def load_author_data(self):
        """Load author information from content/authors/admin/_index.md"""
        author_file = self.content_dir / "authors" / "admin" / "_index.md"
        if author_file.exists():
            self.author_data = self.read_markdown_file(author_file)
            
            # Load avatar if exists
            avatar_path = author_file.parent / "avatar.jpg"
            if avatar_path.exists():
                self.author_data['avatar'] = "avatar.jpg"
    
    def load_publications(self):
        """Load all publications from content/publication/"""
        pub_dir = self.content_dir / "publication"
        if pub_dir.exists():
            for item in pub_dir.iterdir():
                if item.is_dir():
                    index_file = item / "index.md"
                    if index_file.exists():
                        pub_data = self.read_markdown_file(index_file)
                        pub_data['slug'] = item.name
                        
                        # Check for featured image
                        featured_img = item / "featured.png"
                        if featured_img.exists():
                            pub_data['featured_image'] = f"publication/{item.name}/featured.png"
                        
                        self.publications.append(pub_data)
        
        # Sort by date (newest first)
        self.publications.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    def load_projects(self):
        """Load all projects from content/project/"""
        proj_dir = self.content_dir / "project"
        if proj_dir.exists():
            for item in proj_dir.iterdir():
                if item.is_dir():
                    index_file = item / "index.md"
                    if index_file.exists():
                        proj_data = self.read_markdown_file(index_file)
                        proj_data['slug'] = item.name
                        
                        # Check for featured image
                        featured_img = item / "featured.png"
                        if featured_img.exists():
                            proj_data['featured_image'] = f"project/{item.name}/featured.png"
                        
                        # Check for gallery metadata or find additional images
                        if 'gallery' in proj_data:
                            # Use explicit gallery list from metadata
                            proj_data['images'] = [f"project/{item.name}/{img}" for img in proj_data.get('gallery', [])]
                        else:
                            # Fallback to auto-discovery for backward compatibility
                            proj_data['images'] = []
                            for img in item.glob("*.png"):
                                if img.name != "featured.png":
                                    proj_data['images'].append(f"project/{item.name}/{img.name}")
                        
                        self.projects.append(proj_data)
        
        # Sort by date (newest first)
        self.projects.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    def load_config(self):
        """Load site configuration from content/_index.md"""
        config_file = self.content_dir / "_index.md"
        if config_file.exists():
            self.config = self.read_markdown_file(config_file)
    
    def generate_social_links(self) -> str:
        """Generate social media links HTML"""
        social_links = []
        for social in self.author_data.get('social', []):
            icon = social.get('icon', '')
            icon_pack = social.get('icon_pack', 'fas')
            link = social.get('link', '#')
            
            if icon == 'envelope':
                social_links.append(f'<a href="{link}" aria-label="Email"><i class="{icon_pack} fa-{icon}"></i></a>')
            elif icon == 'twitter':
                social_links.append(f'<a href="{link}" aria-label="Twitter"><i class="{icon_pack} fa-{icon}"></i></a>')
            elif icon == 'github':
                social_links.append(f'<a href="{link}" aria-label="GitHub"><i class="{icon_pack} fa-{icon}"></i></a>')
            elif icon == 'linkedin':
                social_links.append(f'<a href="{link}" aria-label="LinkedIn"><i class="{icon_pack} fa-{icon}"></i></a>')
            elif icon == 'cv':
                social_links.append(f'<a href="{link}" aria-label="CV"><i class="ai ai-cv"></i></a>')
        
        return '\n'.join(social_links)
    
    def generate_skills_html(self) -> str:
        """Generate skills section HTML"""
        skills_html = ''
        
        for skill_group in self.author_data.get('skills', []):
            color_class = 'technical' if skill_group.get('name') == 'Technical' else 'hobbies'
            skills_html += f'<div class="skill-column"><h4 class="skill-group-title">{skill_group.get("name", "").upper()}</h4>'
            
            for item in skill_group.get('items', []):
                icon_map = {
                    'Machine Learning/Deep Learning': 'fa-python',
                    'Data Science': 'fa-chart-line',
                    'System/Architecture': 'fa-database',
                    'Phsyics': 'fa-atom',
                    'Hiking': 'fa-person-hiking',
                    'Reading': 'fa-book',
                    'Writing': 'fa-pen',
                    'Cloudherd': 'fa-cloud'
                }
                
                icon = icon_map.get(item.get('name', ''), 'fa-circle')
                icon_pack = item.get('icon_pack', 'fas')
                
                skills_html += f'''
                <div class="skill-item">
                    <div class="skill-header">
                        <i class="{icon_pack} {icon}"></i>
                        <span class="skill-name">{item.get('name', '').upper()}</span>
                    </div>
                    <div class="skill-bar skill-bar-{color_class}">
                        <div class="skill-progress" style="width: {item.get('percent', 0)}%"></div>
                    </div>
                </div>
                '''
            skills_html += '</div>'
        
        return skills_html
    
    def generate_interests_html(self) -> str:
        """Generate interests list HTML"""
        interests_html = ''
        for interest in self.author_data.get('interests', []):
            interests_html += f'<li><i class="fas fa-bookmark"></i> {interest}</li>'
        return interests_html
    
    def generate_education_html(self) -> str:
        """Generate education section HTML"""
        education_html = ''
        for course in self.author_data.get('education', {}).get('courses', []):
            education_html += f'''
            <div class="education-item">
                <i class="fas fa-graduation-cap"></i>
                <div class="education-content">
                    <strong>{course.get('course', '')}, {course.get('year', '')}</strong>
                    <p>{course.get('institution', '')}</p>
                </div>
            </div>
            '''
        return education_html
    
    def format_publication_item(self, pub: dict) -> str:
        """Format a single publication item"""
        authors = ', '.join(pub.get('authors', []))
        
        links = []
        if pub.get('url_pdf'):
            links.append(f'<a href="{pub["url_pdf"]}" class="pub-link"><i class="fas fa-file-pdf"></i> PDF</a>')
        if pub.get('doi'):
            links.append(f'<a href="{pub["doi"]}" class="pub-link"><i class="fas fa-link"></i> DOI</a>')
        for link in pub.get('links', []):
            links.append(f'<a href="{link.get("url", "#")}" class="pub-link"><i class="fas fa-external-link-alt"></i> {link.get("name", "Link")}</a>')
        
        links_html = ' '.join(links)
        
        # Format date
        date_str = pub.get('date', '')
        year = ''
        if date_str:
            try:
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                year = date_obj.year
            except:
                year = ''
        
        return f'''
        <div class="publication-item" data-year="{year}">
            <div class="pub-content">
                <h4 class="pub-title">{pub.get('title', '')}</h4>
                <p class="pub-authors">{authors}</p>
                <p class="pub-venue">{pub.get('publication', '')} {pub.get('publication_short', '')}</p>
                <div class="pub-links">{links_html}</div>
            </div>
            {f'<div class="pub-year">{year}</div>' if year else ''}
        </div>
        '''
    
    def format_project_card(self, proj: dict, base_url: str = '') -> str:
        """Format a project card"""
        image = proj.get('featured_image', 'placeholder.png')
        tags = proj.get('tags', [])
        tags_str = ', '.join(tags)
        
        # Check if project has external link
        external_link = proj.get('external_link', '')
        if external_link:
            # Link directly to external URL
            link = external_link
            link_target = ' target="_blank"'
            link_text = 'View Project →'
        else:
            # Link to project detail page
            link = f"{base_url}projects/{proj['slug']}.html"
            link_target = ''
            link_text = 'View Details →'
        
        # Convert summary markdown to HTML
        summary = proj.get('summary', '')
        summary_html = self.md.convert(summary).replace('<p>', '').replace('</p>', '')
        
        return f'''
        <div class="project-card" data-tags="{tags_str}">
            <img src="{base_url}{image}" alt="{proj.get('title', '')}" class="project-image">
            <div class="project-content">
                <h3>{proj.get('title', '')}</h3>
                <p>{summary_html}</p>
                <div class="project-tags">{tags_str}</div>
                <a href="{link}" class="project-link"{link_target}>{link_text}</a>
            </div>
        </div>
        '''
    
    def generate_contact_html(self) -> str:
        """Generate contact section HTML"""
        # Extract contact info from config
        contact_info = {}
        for section in self.config.get('sections', []):
            if section.get('block') == 'contact':
                contact_info = section.get('content', {})
                break
        
        html = f'<p><i class="fas fa-envelope"></i> {contact_info.get("email", "")}</p>'
        
        address = contact_info.get('address', {})
        if address:
            html += f'''<p><i class="fas fa-map-marker-alt"></i> {address.get('street', '')}, 
                       {address.get('city', '')}, 
                       {address.get('country', '')}</p>'''
        
        if contact_info.get('directions'):
            html += f'<p><i class="fas fa-door-open"></i> {contact_info.get("directions", "")}</p>'
        
        # Add calendar scheduling link
        html += '''<p class="schedule-link"><i class="fas fa-calendar-alt"></i> If you wanna discuss with me, use this tool: 
                   <a href="https://cal.com/yeqi-huang/discussion?duration=30" target="_blank">Schedule a meeting</a></p>'''
        
        return html
    
    def generate_index_page(self):
        """Generate the main index page"""
        template = self.env.get_template('index.html')
        
        # Remove {style="text-align: justify;"} from bio
        bio_html = self.author_data.get('content_html', '').replace('{style="text-align: justify;"}', '')
        
        context = {
            'title': self.author_data.get('name_pronunciation', 'Personal Homepage'),
            'site_title': 'Personal Homepage',
            'author_name': self.author_data.get('name_pronunciation', 'Your Name'),
            'year': datetime.now().year,
            'base_url': '',
            
            # Hero section
            'name_pronunciation': self.author_data.get('title', ''),
            'role': self.author_data.get('role', ''),
            'org_name': self.author_data.get('organizations', [{}])[0].get('name', ''),
            'org_url': self.author_data.get('organizations', [{}])[0].get('url', '#'),
            'social_links': self.generate_social_links(),
            'bio_content': bio_html,
            
            # About section
            'skills_content': self.generate_skills_html(),
            'interests_content': self.generate_interests_html(),
            'education_content': self.generate_education_html(),
            
            # Publications preview (latest 10)
            'publications_preview': ''.join([self.format_publication_item(pub) for pub in self.publications[:10]]),
            
            # Projects preview (latest 6)
            'projects_preview': ''.join([self.format_project_card(proj) for proj in self.projects[:6]]),
            
            # Contact
            'contact_content': self.generate_contact_html()
        }
        
        html = template.render(context)
        
        with open(self.output_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(html)
    
    def generate_publications_page(self):
        """Generate the publications listing page"""
        template = self.env.get_template('publications.html')
        
        # Generate year filters
        years = set()
        for pub in self.publications:
            date_str = pub.get('date', '')
            if date_str:
                try:
                    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    years.add(date_obj.year)
                except:
                    pass
        
        year_filters = ''
        for year in sorted(years, reverse=True):
            year_filters += f'<span class="filter-tag" data-year="{year}">{year}</span>'
        
        context = {
            'title': 'Publications',
            'site_title': 'Personal Homepage',
            'author_name': self.author_data.get('name_pronunciation', 'Your Name'),
            'year': datetime.now().year,
            'base_url': '',
            'publications_content': ''.join([self.format_publication_item(pub) for pub in self.publications]),
            'year_filters': year_filters
        }
        
        html = template.render(context)
        
        with open(self.output_dir / "publications.html", 'w', encoding='utf-8') as f:
            f.write(html)
    
    def generate_projects_page(self):
        """Generate the projects listing page"""
        template = self.env.get_template('projects.html')
        
        # Generate tag filters
        tags = set()
        for proj in self.projects:
            for tag in proj.get('tags', []):
                tags.add(tag)
        
        tag_filters = ''
        for tag in sorted(tags):
            tag_filters += f'<span class="filter-tag" data-tag="{tag}">{tag}</span>'
        
        context = {
            'title': 'Projects',
            'site_title': 'Personal Homepage',
            'author_name': self.author_data.get('name_pronunciation', 'Your Name'),
            'year': datetime.now().year,
            'base_url': '',
            'projects_content': ''.join([self.format_project_card(proj) for proj in self.projects]),
            'tag_filters': tag_filters
        }
        
        html = template.render(context)
        
        with open(self.output_dir / "projects.html", 'w', encoding='utf-8') as f:
            f.write(html)
    
    def generate_project_detail_pages(self):
        """Generate individual project detail pages"""
        template = self.env.get_template('project_detail.html')
        
        # Create projects directory
        projects_dir = self.output_dir / "projects"
        projects_dir.mkdir(exist_ok=True)
        
        for proj in self.projects:
            # Generate page for all projects
            
            # Format tags
            tags_html = ''
            for tag in proj.get('tags', []):
                tags_html += f'<span>{tag}</span>'
            
            # Format gallery images
            images_html = ''
            for img in proj.get('images', []):
                images_html += f'<img src="../{img}" alt="{proj.get("title", "")} screenshot">'
            
            context = {
                'title': proj.get('title', 'Project'),
                'site_title': 'Personal Homepage',
                'author_name': self.author_data.get('name_pronunciation', 'Your Name'),
                'year': datetime.now().year,
                'base_url': '../',
                'project_title': proj.get('title', ''),
                'project_tags': tags_html,
                'external_link': proj.get('external_link', ''),
                'featured_image': f"../{proj.get('featured_image', '')}" if proj.get('featured_image') else None,
                'project_content': proj.get('content_html', ''),
                'project_images': images_html if images_html else None
            }
            
            html = template.render(context)
            
            with open(projects_dir / f"{proj['slug']}.html", 'w', encoding='utf-8') as f:
                f.write(html)
    
    def copy_static_files(self):
        """Copy CSS and JS files from templates to dist"""
        # Copy CSS
        css_src = self.template_dir / "style.css"
        if css_src.exists():
            shutil.copy(css_src, self.output_dir / "style.css")
        
        # Copy JS
        js_src = self.template_dir / "script.js"
        if js_src.exists():
            shutil.copy(js_src, self.output_dir / "script.js")
    
    
    def copy_assets(self):
        """Copy images and other assets to output directory"""
        # Copy author avatar
        avatar_src = self.content_dir / "authors" / "admin" / "avatar.jpg"
        if avatar_src.exists():
            shutil.copy(avatar_src, self.output_dir / "avatar.jpg")
        
        # Copy project images
        proj_dir = self.content_dir / "project"
        if proj_dir.exists():
            output_proj_dir = self.output_dir / "project"
            output_proj_dir.mkdir(parents=True, exist_ok=True)
            
            for item in proj_dir.iterdir():
                if item.is_dir():
                    item_output = output_proj_dir / item.name
                    item_output.mkdir(exist_ok=True)
                    
                    # Copy all images (png and jpg)
                    for img in item.glob("*.png"):
                        shutil.copy(img, item_output / img.name)
                    for img in item.glob("*.jpg"):
                        shutil.copy(img, item_output / img.name)
                    for img in item.glob("*.jpeg"):
                        shutil.copy(img, item_output / img.name)
        
        # Copy publication images
        pub_dir = self.content_dir / "publication"
        if pub_dir.exists():
            output_pub_dir = self.output_dir / "publication"
            output_pub_dir.mkdir(parents=True, exist_ok=True)
            
            for item in pub_dir.iterdir():
                if item.is_dir():
                    item_output = output_pub_dir / item.name
                    item_output.mkdir(exist_ok=True)
                    
                    # Copy featured image
                    featured = item / "featured.png"
                    if featured.exists():
                        shutil.copy(featured, item_output / "featured.png")
        
        # Copy CV if exists
        cv_src = self.content_dir / "resume.pdf"
        if cv_src.exists():
            uploads_dir = self.output_dir / "uploads"
            uploads_dir.mkdir(exist_ok=True)
            shutil.copy(cv_src, uploads_dir / "resume.pdf")
    
    def generate(self):
        """Main generation process"""
        print("Starting homepage generation...")
        
        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        
        # Load all content
        print("Loading content...")
        self.load_author_data()
        self.load_publications()
        self.load_projects()
        self.load_config()
        
        # Generate pages
        print("Generating pages...")
        self.generate_index_page()
        self.generate_publications_page()
        self.generate_projects_page()
        self.generate_project_detail_pages()
        
        # Copy CSS and JS
        print("Copying static files...")
        self.copy_static_files()
        
        # Copy assets
        print("Copying assets...")
        self.copy_assets()
        
        print(f"Homepage generated successfully in {self.output_dir}/")
        print(f"Open {self.output_dir}/index.html in your browser to view.")


if __name__ == "__main__":
    generator = PersonalHomepageGenerator()
    generator.generate()