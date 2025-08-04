# Personal Homepage Generator

A Python-based static site generator that creates a modern, responsive personal homepage from markdown content.

## Features

- 🎨 Modern, clean design inspired by academic portfolio sites
- 📱 Fully responsive layout
- 🌙 Dark/Light theme switcher
- 📝 Markdown-based content management
- 🚀 Fast static site generation
- 🔧 Easy customization

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your content is organized in the `content/` directory following the Hugo Blox structure
2. Run the generator:
```bash
python generator.py
```
3. Your generated site will be in the `dist/` directory
4. Open `dist/index.html` in your browser to view

## Content Structure

The generator expects content organized as follows:
```
content/
├── _index.md                 # Site configuration
├── authors/
│   └── admin/
│       ├── _index.md        # Your profile information
│       └── avatar.jpg       # Profile photo
├── publication/
│   └── paper-name/
│       ├── index.md         # Publication details
│       └── featured.png     # Publication image
└── project/
    └── project-name/
        ├── index.md         # Project details
        └── featured.png     # Project image
```

## Customization

- Modify `generator.py` to change the HTML structure
- Edit the CSS generation in `generate_css()` method
- Add new sections by extending the generator class

## Output

The generator creates:
- `index.html` - Main homepage
- `style.css` - Styling
- `script.js` - Interactive features
- Asset copies (images, PDFs)