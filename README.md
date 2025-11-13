# Personal Homepage

A Python-based static site generator for creating modern, responsive personal academic homepages. This tool converts markdown content into a beautiful static website featuring your publications, projects, bio, and contact information.

## Features

- **Modern Design** - Clean, professional layout inspired by academic portfolio sites
- **Fully Responsive** - Works seamlessly on desktop, tablet, and mobile devices
- **Dark/Light Theme** - Built-in theme switcher for user preference
- **Markdown-Based** - Write content in markdown with YAML frontmatter
- **Publications Management** - Showcase your research papers with filtering by year
- **Project Portfolio** - Display your projects with tags, images, and detailed pages
- **Fast Generation** - Efficient static site generation using Jinja2 templates
- **Easy Customization** - Template-based architecture for easy modifications

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Personal-Page
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

1. Ensure your content is organized in the `content/` directory
2. Run the generator:
```bash
python generator.py
```
3. Your generated site will be in the `dist/` directory
4. Open `dist/index.html` in your browser to preview

## Content Structure

The generator expects content organized as follows:

```
content/
├── _index.md                      # Site configuration
├── authors/
│   └── admin/
│       ├── _index.md              # Your profile information
│       └── avatar.jpg             # Profile photo
├── publication/
│   └── paper-name/
│       ├── index.md               # Publication details
│       └── featured.png           # Publication image (optional)
├── project/
│   └── project-name/
│       ├── index.md               # Project details
│       ├── featured.png           # Project thumbnail
│       └── *.png                  # Additional project images
└── resume.pdf                     # Your CV (optional)
```

### Content File Format

#### Author Profile (`content/authors/admin/_index.md`)

```yaml
---
title: Your Name
name_pronunciation: Your Name
role: PhD Student in Computer Science
organizations:
  - name: Your University
    url: https://university.edu/

bio: Brief bio here

interests:
  - Research Area 1
  - Research Area 2

education:
  courses:
    - course: PhD in Computer Science
      institution: University Name
      year: 2023

social:
  - icon: envelope
    icon_pack: fas
    link: mailto:your@email.com
  - icon: github
    icon_pack: fab
    link: https://github.com/username
---

Your detailed biography in markdown format...
```

#### Publications (`content/publication/paper-name/index.md`)

```yaml
---
title: "Paper Title"
authors:
  - Author 1
  - Author 2
date: "2024-01-01"
publication: "Conference/Journal Name"
publication_short: "CONF'24"
url_pdf: "path/to/paper.pdf"
doi: "https://doi.org/..."
---

Paper abstract and details...
```

#### Projects (`content/project/project-name/index.md`)

```yaml
---
title: "Project Name"
summary: "Brief project description"
tags:
  - Machine Learning
  - Web Development
date: "2024-01-01"
external_link: "https://project-url.com"
github_link: "https://github.com/user/project"
---

Detailed project description in markdown...
```

## Generated Site Structure

After running the generator, the following structure is created:

```
dist/
├── index.html                 # Main homepage
├── publications.html          # Publications listing
├── projects.html              # Projects listing
├── projects/
│   └── [project-slug].html   # Individual project pages
├── style.css                  # Compiled styles
├── script.js                  # Interactive features
├── avatar.jpg                 # Profile photo
├── project/                   # Project images
├── publication/               # Publication images
└── uploads/
    └── resume.pdf            # Your CV
```

## Customization

### Modifying Templates

Templates are located in the `templates/` directory:

- `base.html` - Base template with common structure
- `index.html` - Homepage template
- `publications.html` - Publications page template
- `projects.html` - Projects listing template
- `project_detail.html` - Individual project page template

### Styling

Edit `templates/style.css` to customize the visual appearance.

### Functionality

Modify `templates/script.js` to add or change interactive features.

### Generator Logic

Edit `generator.py` to:
- Change the HTML structure
- Add new sections
- Modify data processing
- Customize filtering or sorting

## Deployment

### GitHub Pages

1. Generate your site:
```bash
python generator.py
```

2. Deploy the `dist/` directory to GitHub Pages:
```bash
# Option 1: Manual deployment
cp -r dist/* docs/
git add docs/
git commit -m "Update site"
git push

# Option 2: Use gh-pages branch
git checkout -b gh-pages
cp -r dist/* .
git add .
git commit -m "Deploy site"
git push origin gh-pages
```

### Other Hosting

Upload the contents of the `dist/` directory to any static hosting service:
- Netlify
- Vercel
- AWS S3
- Azure Static Web Apps
- Cloudflare Pages

## Development

To work on the generator:

1. Make changes to `generator.py` or templates
2. Test your changes:
```bash
python generator.py
```
3. View the results by opening `dist/index.html`

## Features in Detail

### Publications Page
- Automatic year extraction from publication dates
- Filter publications by year
- Links to PDF, DOI, and custom links
- Responsive card layout

### Projects Page
- Tag-based filtering
- Project cards with images
- Links to GitHub, external sites, or detail pages
- Image galleries on detail pages

### About Section
- Skills visualization with progress bars
- Education timeline
- Research interests
- Social media links

### Theme Switcher
- Dark and light mode support
- User preference persistence
- Smooth transitions

## Dependencies

- **markdown** (>=3.4.0) - Markdown processing with extensions
- **PyYAML** (>=6.0) - YAML frontmatter parsing
- **Pygments** (>=2.16.0) - Syntax highlighting
- **Jinja2** (>=3.1.0) - Template rendering

## Troubleshooting

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

### Missing Content
Ensure your markdown files have proper YAML frontmatter enclosed in `---`.

### Images Not Showing
Check that image paths in your markdown files are relative to the content directory.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

This generator is designed to work with content structured for Hugo Blox (formerly Hugo Academic), making it easy to migrate or maintain compatibility.

## Contact

For questions or feedback, please open an issue on GitHub.
