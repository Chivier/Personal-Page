# Personal Homepage

Static personal academic homepage with bilingual support (English/Chinese), built with a Python generator and Jinja2 templates.

## Architecture

- `generator.py` — Main build script. Reads markdown content, compiles templates, optionally compiles CV via xelatex, outputs to `dist/`.
- `templates/` — Jinja2 HTML templates + CSS/JS.
- `content/` — Markdown source files with YAML frontmatter.
  - `content/authors/admin/_index.md` — Author bio (English). `_index.zh.md` for Chinese.
  - `content/publication/<slug>/index.md` — One directory per publication.
  - `content/project/<slug>/index.md` — One directory per project.
- `i18n/en.yml`, `i18n/zh.yml` — UI translation strings.
- `CV-Overleaf/` — LaTeX CV source. Compiled with xelatex (uses `ctex` package). Output PDF is copied to `dist/uploads/resume.pdf`.
- `dist/` — Generated output (gitignored). English at root, Chinese at `dist/zh/`.

## Build

```bash
# Install Python deps
pip install -r requirements.txt

# Generate site (also compiles CV if xelatex is available)
python generator.py
```

Local preview: open `dist/index.html` in a browser.

## CV Compilation

The generator starts xelatex in the background while building HTML pages. If xelatex is not installed locally, it gracefully skips compilation but still copies `CV-Overleaf/main.pdf` if it exists.

In CI, `xu-cheng/latex-action@v3` compiles the CV before `generator.py` runs.

## CI/CD

GitHub Actions workflow at `.github/workflows/deploy.yml`:
1. Compiles CV with xelatex (via latex-action, `continue-on-error: true`)
2. Installs Python deps
3. Runs `python generator.py`
4. Deploys `dist/` to GitHub Pages

## Adding Content

### New publication
Create `content/publication/<slug>/index.md` with frontmatter:
```yaml
---
title: "Paper Title"
authors: ["Author One", "Author Two"]
date: "2026-01-01T00:00:00Z"
publication: "Conference Name"
publication_short: "CONF'26"
url_pdf: ""
---
```

### New project
Create `content/project/<slug>/index.md` with similar frontmatter. Add `featured.png` for the card image.

## Key Conventions

- All templates use `{{ t.section.key }}` for translated UI strings.
- Publication/project entries are sorted by `date` descending.
- The CV social link points to `uploads/resume.pdf` (relative path).
