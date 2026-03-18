#!/usr/bin/env python3
"""
Personal Homepage Generator V2 - Template-based
Generates a static personal homepage from markdown content using Jinja2 templates
Supports bilingual output (English + Chinese)
"""

import os
import json
import yaml
import markdown
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import shutil
from jinja2 import Environment, FileSystemLoader


class PersonalHomepageGenerator:
    SUPPORTED_LANGS = ['en', 'zh']
    DEFAULT_LANG = 'en'

    def __init__(self, content_dir: str = "content", output_dir: str = "dist", template_dir: str = "templates"):
        self.content_dir = Path(content_dir)
        self.output_dir = Path(output_dir)
        self.template_dir = Path(template_dir)
        self.i18n_dir = Path("i18n")

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

        # Data storage (per language)
        self.author_data = {}
        self.publications = []
        self.projects = []
        self.config = {}
        self.translations = {}

    def load_translations(self):
        """Load translation files for all supported languages"""
        for lang in self.SUPPORTED_LANGS:
            lang_file = self.i18n_dir / f"{lang}.yml"
            if lang_file.exists():
                with open(lang_file, 'r', encoding='utf-8') as f:
                    self.translations[lang] = yaml.safe_load(f)
            else:
                self.translations[lang] = {}

    def get_translations(self, lang: str) -> dict:
        """Get translation dictionary for a language"""
        return self.translations.get(lang, self.translations.get(self.DEFAULT_LANG, {}))

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
        self.md.reset()
        meta['content_html'] = self.md.convert(body)
        meta['content_raw'] = body

        return meta

    def load_author_data(self, lang: str = 'en'):
        """Load author information, preferring language-specific file"""
        # Try language-specific file first
        if lang != self.DEFAULT_LANG:
            lang_file = self.content_dir / "authors" / "admin" / f"_index.{lang}.md"
            if lang_file.exists():
                self.author_data = self.read_markdown_file(lang_file)
                avatar_path = lang_file.parent / "avatar.jpg"
                if avatar_path.exists():
                    self.author_data['avatar'] = "avatar.jpg"
                return

        # Fallback to default
        author_file = self.content_dir / "authors" / "admin" / "_index.md"
        if author_file.exists():
            self.author_data = self.read_markdown_file(author_file)
            avatar_path = author_file.parent / "avatar.jpg"
            if avatar_path.exists():
                self.author_data['avatar'] = "avatar.jpg"

    def load_publications(self):
        """Load all publications from content/publication/"""
        self.publications = []
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
        self.projects = []
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
                            proj_data['images'] = [f"project/{item.name}/{img}" for img in proj_data.get('gallery', [])]
                        else:
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

    def generate_social_links(self, base_url: str = '') -> str:
        """Generate social media links HTML"""
        social_links = []
        for social in self.author_data.get('social', []):
            icon = social.get('icon', '')
            icon_pack = social.get('icon_pack', 'fas')
            link = social.get('link', '#')

            # Adjust relative links for subdirectory
            if link.startswith('/') or link.startswith('#'):
                link = base_url + link.lstrip('/')

            if icon_pack == 'ai':
                # Academicons (google-scholar, cv, etc.)
                if icon == 'cv' and not link.startswith('http'):
                    link = base_url + link
                label = icon.replace('-', ' ').title()
                social_links.append(f'<a href="{link}" aria-label="{label}"><i class="ai ai-{icon}"></i></a>')
            elif icon == 'envelope':
                social_links.append(f'<a href="{link}" aria-label="Email"><i class="{icon_pack} fa-{icon}"></i></a>')
            else:
                label = icon.replace('-', ' ').title()
                social_links.append(f'<a href="{link}" aria-label="{label}"><i class="{icon_pack} fa-{icon}"></i></a>')

        return '\n'.join(social_links)

    def generate_skills_html(self) -> str:
        """Generate skills section HTML"""
        skills_html = ''

        for skill_group in self.author_data.get('skills', []):
            # Use first group as technical, second as hobbies
            name = skill_group.get('name', '')
            # Determine color class based on position (first = technical, others = hobbies)
            color_class = 'technical' if skill_group == self.author_data.get('skills', [])[0] else 'hobbies'
            skills_html += f'<div class="skill-column"><h4 class="skill-group-title">{name.upper()}</h4>'

            for item in skill_group.get('items', []):
                icon_map = {
                    'Machine Learning/Deep Learning': 'fa-python',
                    '机器学习/深度学习': 'fa-python',
                    'Data Science': 'fa-chart-line',
                    '数据科学': 'fa-chart-line',
                    'System/Architecture': 'fa-database',
                    '系统/架构': 'fa-database',
                    'Phsyics': 'fa-atom',
                    '物理': 'fa-atom',
                    'Hiking': 'fa-person-hiking',
                    '徒步': 'fa-person-hiking',
                    'Reading': 'fa-book',
                    '阅读': 'fa-book',
                    'Writing': 'fa-pen',
                    '写作': 'fa-pen',
                    'Cloudherd': 'fa-cloud',
                    '云牧': 'fa-cloud'
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

    def format_project_card(self, proj: dict, base_url: str = '', t: dict = None) -> str:
        """Format a project card"""
        image = proj.get('featured_image', 'placeholder.png')
        tags = proj.get('tags', [])
        tags_str = ', '.join(tags)

        # Generate individual tag spans with styling
        tags_html = ' '.join([f'<span class="project-tag">{tag}</span>' for tag in tags])

        # Build link buttons
        links_html = '<div class="project-links">'

        # Get translated text
        view_project_text = 'View Project'
        view_details_text = 'View Details →'
        if t:
            view_project_text = t.get('project_detail', {}).get('view_project', view_project_text)
            view_details_text = t.get('project_detail', {}).get('view_details', view_details_text)

        # Check for GitHub link
        github_link = proj.get('github_link', '')
        if github_link:
            links_html += f'<a href="{github_link}" class="project-link github-link" target="_blank"><i class="fab fa-github"></i> GitHub</a>'

        # Check for external link
        external_link = proj.get('external_link', '')
        if external_link:
            links_html += f'<a href="{external_link}" class="project-link external-link" target="_blank"><i class="fas fa-external-link-alt"></i> {view_project_text}</a>'
        elif not github_link:
            # If no external or github link, show detail page link
            link = f"{base_url}projects/{proj['slug']}.html"
            links_html += f'<a href="{link}" class="project-link">{view_details_text}</a>'

        links_html += '</div>'

        # Convert summary markdown to HTML
        summary = proj.get('summary', '')
        self.md.reset()
        summary_html = self.md.convert(summary).replace('<p>', '').replace('</p>', '')

        return f'''
        <div class="project-card" data-tags="{tags_str}">
            <img src="{base_url}{image}" alt="{proj.get('title', '')}" class="project-image">
            <div class="project-content">
                <h3>{proj.get('title', '')}</h3>
                <p>{summary_html}</p>
                <div class="project-tags">{tags_html}</div>
                {links_html}
            </div>
        </div>
        '''

    def generate_schedule_html(self, t: dict = None, variant: str = 'hero') -> str:
        """Generate schedule/booking HTML.

        variant:
          - hero: compact button-style for top of page
          - contact: inline text for contact section
        """
        schedule_text = 'If you wanna discuss with me, use this tool:'
        schedule_link_text = 'Schedule a meeting'
        if t:
            schedule_text = t.get('contact', {}).get('schedule_text', schedule_text)
            schedule_link_text = t.get('contact', {}).get('schedule_link', schedule_link_text)

        url = "https://cal.com/yeqi-huang/discussion?duration=30"

        if variant == 'contact':
            return (
                f'''<p class="schedule-link"><i class="fas fa-calendar-alt"></i> {schedule_text} '''
                f'''<a href="{url}" target="_blank">{schedule_link_text}</a></p>'''
            )

        # hero
        return (
            f'''<a class="schedule-btn" href="{url}" target="_blank">'''
            f'''<i class="fas fa-calendar-alt"></i> {schedule_link_text}</a>'''
        )

    def generate_contact_html(self, t: dict = None) -> str:
        """Generate contact section HTML (email/address only; scheduling is shown earlier)."""
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

        return html

    def get_lang_switch_url(self, lang: str, page: str = 'index.html') -> str:
        """Get the URL to switch to the other language"""
        if lang == 'en':
            return f"zh/{page}"
        else:
            return f"../{page}"

    def get_base_context(self, lang: str, base_url: str = '', page: str = 'index.html') -> dict:
        """Get common context for all pages"""
        t = self.get_translations(lang)
        return {
            'site_title': t.get('site', {}).get('title', 'Personal Homepage'),
            'author_name': self.author_data.get('name_pronunciation', 'Your Name'),
            'year': datetime.now().year,
            'base_url': base_url,
            't': t,
            'lang': lang,
            'lang_switch_url': self.get_lang_switch_url(lang, page),
        }

    def generate_index_page(self, lang: str = 'en', output_dir: Path = None):
        """Generate the main index page"""
        if output_dir is None:
            output_dir = self.output_dir

        template = self.env.get_template('index.html')
        t = self.get_translations(lang)
        base_url = '' if lang == self.DEFAULT_LANG else '../'

        # Remove {style="text-align: justify;"} from bio
        bio_html = self.author_data.get('content_html', '').replace('{style="text-align: justify;"}', '')

        context = self.get_base_context(lang, base_url, 'index.html')
        context.update({
            'title': self.author_data.get('name_pronunciation', t.get('site', {}).get('title', 'Personal Homepage')),

            # Hero section
            'name_pronunciation': self.author_data.get('title', ''),
            'role': self.author_data.get('role', ''),
            'org_name': self.author_data.get('organizations', [{}])[0].get('name', ''),
            'org_url': self.author_data.get('organizations', [{}])[0].get('url', '#'),
            'social_links': self.generate_social_links(base_url),
            'schedule_html': self.generate_schedule_html(t, variant='hero'),
            'bio_content': bio_html,

            # About section
            'skills_content': self.generate_skills_html(),
            'interests_content': self.generate_interests_html(),
            'education_content': self.generate_education_html(),

            # Publications preview (latest 10)
            'publications_preview': ''.join([self.format_publication_item(pub) for pub in self.publications[:10]]),

            # Projects preview (latest 6)
            'projects_preview': ''.join([self.format_project_card(proj, base_url, t) for proj in self.projects[:6]]),

            # Contact
            'contact_content': self.generate_contact_html(t)
        })

        html = template.render(context)

        with open(output_dir / "index.html", 'w', encoding='utf-8') as f:
            f.write(html)

    def generate_publications_page(self, lang: str = 'en', output_dir: Path = None):
        """Generate the publications listing page"""
        if output_dir is None:
            output_dir = self.output_dir

        template = self.env.get_template('publications.html')
        t = self.get_translations(lang)
        base_url = '' if lang == self.DEFAULT_LANG else '../'

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

        context = self.get_base_context(lang, base_url, 'publications.html')
        context.update({
            'title': t.get('publications', {}).get('title', 'Publications'),
            'publications_content': ''.join([self.format_publication_item(pub) for pub in self.publications]),
            'year_filters': year_filters
        })

        html = template.render(context)

        with open(output_dir / "publications.html", 'w', encoding='utf-8') as f:
            f.write(html)

    def generate_projects_page(self, lang: str = 'en', output_dir: Path = None):
        """Generate the projects listing page"""
        if output_dir is None:
            output_dir = self.output_dir

        template = self.env.get_template('projects.html')
        t = self.get_translations(lang)
        base_url = '' if lang == self.DEFAULT_LANG else '../'

        # Generate tag filters
        tags = set()
        for proj in self.projects:
            for tag in proj.get('tags', []):
                tags.add(tag)

        tag_filters = ''
        for tag in sorted(tags):
            tag_filters += f'<span class="filter-tag" data-tag="{tag}">{tag}</span>'

        context = self.get_base_context(lang, base_url, 'projects.html')
        context.update({
            'title': t.get('projects', {}).get('title', 'Projects'),
            'projects_content': ''.join([self.format_project_card(proj, base_url, t) for proj in self.projects]),
            'tag_filters': tag_filters
        })

        html = template.render(context)

        with open(output_dir / "projects.html", 'w', encoding='utf-8') as f:
            f.write(html)

    def generate_project_detail_pages(self, lang: str = 'en', output_dir: Path = None):
        """Generate individual project detail pages"""
        if output_dir is None:
            output_dir = self.output_dir

        template = self.env.get_template('project_detail.html')
        t = self.get_translations(lang)
        base_url = '' if lang == self.DEFAULT_LANG else '../'
        # For detail pages, we need one more level up
        detail_base_url = '../' if lang == self.DEFAULT_LANG else '../../'

        # Create projects directory
        projects_dir = output_dir / "projects"
        projects_dir.mkdir(exist_ok=True)

        for proj in self.projects:
            # Format tags
            tags_html = ''
            for tag in proj.get('tags', []):
                tags_html += f'<span>{tag}</span>'

            # Format gallery images
            images_html = ''
            for img in proj.get('images', []):
                images_html += f'<img src="{detail_base_url}{img}" alt="{proj.get("title", "")} screenshot">'

            context = self.get_base_context(lang, detail_base_url, f'projects/{proj["slug"]}.html')
            # Fix lang switch URL for detail pages
            if lang == 'en':
                context['lang_switch_url'] = f"../../zh/projects/{proj['slug']}.html"
            else:
                context['lang_switch_url'] = f"../../projects/{proj['slug']}.html"

            context.update({
                'title': proj.get('title', 'Project'),
                'project_title': proj.get('title', ''),
                'project_tags': tags_html,
                'external_link': proj.get('external_link', ''),
                'featured_image': f"{detail_base_url}{proj.get('featured_image', '')}" if proj.get('featured_image') else None,
                'project_content': proj.get('content_html', ''),
                'project_images': images_html if images_html else None
            })

            html = template.render(context)

            with open(projects_dir / f"{proj['slug']}.html", 'w', encoding='utf-8') as f:
                f.write(html)

    def copy_static_files(self, output_dir: Path = None):
        """Copy CSS and JS files from templates to dist"""
        if output_dir is None:
            output_dir = self.output_dir

        # Copy CSS
        css_src = self.template_dir / "style.css"
        if css_src.exists():
            shutil.copy(css_src, output_dir / "style.css")

        # Copy JS
        js_src = self.template_dir / "script.js"
        if js_src.exists():
            shutil.copy(js_src, output_dir / "script.js")

    def copy_assets(self, output_dir: Path = None):
        """Copy images and other assets to output directory"""
        if output_dir is None:
            output_dir = self.output_dir

        # Copy author avatar
        avatar_src = self.content_dir / "authors" / "admin" / "avatar.jpg"
        if avatar_src.exists():
            shutil.copy(avatar_src, output_dir / "avatar.jpg")

        # Copy project images
        proj_dir = self.content_dir / "project"
        if proj_dir.exists():
            output_proj_dir = output_dir / "project"
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
            output_pub_dir = output_dir / "publication"
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
            uploads_dir = output_dir / "uploads"
            uploads_dir.mkdir(exist_ok=True)
            shutil.copy(cv_src, uploads_dir / "resume.pdf")

    def generate_for_language(self, lang: str):
        """Generate all pages for a specific language"""
        if lang == self.DEFAULT_LANG:
            output_dir = self.output_dir
        else:
            output_dir = self.output_dir / lang
            output_dir.mkdir(parents=True, exist_ok=True)

        # Load language-specific author data
        self.load_author_data(lang)

        # Generate pages
        print(f"  Generating {lang} pages...")
        self.generate_index_page(lang, output_dir)
        self.generate_publications_page(lang, output_dir)
        self.generate_projects_page(lang, output_dir)
        self.generate_project_detail_pages(lang, output_dir)

        # For non-default language, copy static files and assets to subdirectory
        # so relative paths work correctly
        if lang != self.DEFAULT_LANG:
            self.copy_static_files(output_dir)
            self.copy_assets(output_dir)

    def compile_cv(self) -> list[subprocess.Popen]:
        """Start xelatex compilation of CVs in the background. Returns process handles."""
        cv_dir = Path("CV-Overleaf")
        procs = []
        for tex_name in ["main.tex", "main_zh.tex"]:
            tex_file = cv_dir / tex_name
            if not tex_file.exists():
                continue
            print(f"Starting CV compilation ({tex_name})...")
            try:
                proc = subprocess.Popen(
                    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex_name],
                    cwd=cv_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                )
                procs.append((tex_name, proc))
            except FileNotFoundError:
                print("Warning: xelatex not found, skipping CV compilation.")
                break
        return procs

    def collect_cv(self, procs: list):
        """Wait for CV compilations to finish and copy PDFs to dist/uploads/."""
        for tex_name, proc in procs:
            stdout, _ = proc.communicate()
            pdf_name = tex_name.replace(".tex", ".pdf")
            if proc.returncode != 0:
                print(f"Warning: xelatex compilation failed for {tex_name}:")
                print(stdout.decode(errors="replace")[-2000:])
            else:
                print(f"CV compilation succeeded: {pdf_name}")

        # Copy English CV to both en and zh dist
        cv_dir = Path("CV-Overleaf")
        pdf_en = cv_dir / "main.pdf"
        pdf_zh = cv_dir / "main_zh.pdf"

        if pdf_en.exists():
            uploads = self.output_dir / "uploads"
            uploads.mkdir(parents=True, exist_ok=True)
            shutil.copy(pdf_en, uploads / "resume.pdf")
            # Also copy to zh if no Chinese CV
            zh_uploads = self.output_dir / "zh" / "uploads"
            zh_uploads.mkdir(parents=True, exist_ok=True)
            if pdf_zh.exists():
                shutil.copy(pdf_zh, zh_uploads / "resume.pdf")
            else:
                shutil.copy(pdf_en, zh_uploads / "resume.pdf")
            print("CV PDFs copied to dist/uploads/")
        else:
            print("Warning: No CV PDF found at CV-Overleaf/main.pdf")

    def generate(self):
        """Main generation process"""
        print("Starting homepage generation...")

        # Create output directory
        self.output_dir.mkdir(exist_ok=True)

        # Start CV compilation early (runs in background)
        cv_proc = self.compile_cv()

        # Load translations
        print("Loading translations...")
        self.load_translations()

        # Load shared content (publications, projects, config)
        print("Loading content...")
        self.load_publications()
        self.load_projects()
        self.load_config()

        # Generate pages for each language
        for lang in self.SUPPORTED_LANGS:
            self.generate_for_language(lang)

        # Copy static files and assets to root (for default language)
        print("Copying static files...")
        self.copy_static_files()

        print("Copying assets...")
        self.copy_assets()

        # Copy CNAME file for GitHub Pages custom domain
        cname_src = Path("CNAME")
        if cname_src.exists():
            shutil.copy(cname_src, self.output_dir / "CNAME")
            print("CNAME copied to dist/")

        # Wait for CV compilation and copy result
        self.collect_cv(cv_proc)

        print(f"Homepage generated successfully in {self.output_dir}/")
        print(f"  English: {self.output_dir}/index.html")
        print(f"  Chinese: {self.output_dir}/zh/index.html")


if __name__ == "__main__":
    generator = PersonalHomepageGenerator()
    generator.generate()
